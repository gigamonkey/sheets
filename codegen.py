#!/usr/bin/env python

import json
import re
import sys
from collections import Counter
from collections import defaultdict
from dataclasses import dataclass

type_mapping = {
    "any": "Any",
    "boolean": "bool",
    "double": "float",
    "float": "float",
    "integer": "int",
    "string": "str",
}


def say(x):
    print(x, file=sys.stderr)


def walk_properties(schemas, fn):
    def walk_type(parent, property_name, p, fn):
        if "type" in p:
            t = p["type"]
            if t == "array":
                yield from walk_type(parent, property_name, p["items"], fn)
            else:
                yield from fn(parent, property_name, p)

    for name, spec in schemas.items():
        properties = spec["properties"]
        for n, p in properties.items():
            yield from walk_type(name, n, p, fn)


def enum_names(schemas):
    def enum_values(parent, key, p):
        if "enum" in p:
            yield (parent, key, tuple(p["enum"]))

    enums = defaultdict(list)
    for parent, key, values in walk_properties(schemas, enum_values):
        enums[values].append((parent, key))
    return {values: enum_name(values, names) for values, names in enums.items()}


def enum_name(values, names):
    if from_first_value := enum_name_from_unpecified(values[0]):
        return from_first_value
    elif len(suffix := common_suffix(n[1] for n in names)) > 3:
        # Kludge to deal with one unfortunate type.
        if suffix == "Type" and enum_most_common(names) == "pasteType":
            return "PasteType"
        else:
            return upcase_first(suffix)
    else:
        return upcase_first(enum_most_common(names))


def enum_name_from_unpecified(u):
    # A lot of the enum types in the discovery document have a special
    # first value which also maps to a good name for the type of the enum.
    for end in ("_UNSPECIFIED", "_UNDEFINED"):
        if u.endswith(end):
            return u[: -len(end)].replace("_", " ").title().replace(" ", "")
    return None


def enum_most_common(names):
    return Counter(n[1] for n in names).most_common(1)[0][0]


def upcase_first(s):
    return f"{s[0].upper()}{s[1:]}"


def zipmany(xs):
    done = False
    iters = [iter(x) for x in xs]
    while not done:
        try:
            yield [next(i) for i in iters]
        except StopIteration:
            done = True


def common_suffix(names):
    s = []
    for nexts in zipmany((reversed(n) for n in names)):
        unique = {c.lower() for c in nexts}
        if len(unique) == 1:
            if any(c.isupper() for c in nexts):
                s.append(unique.pop().upper())
            else:
                s.append(unique.pop())
        else:
            break
    return "".join(reversed(s))


def emit_typed_dict(spec, enums):
    name = spec["id"]
    description = spec["description"]
    properties = spec["properties"]

    print(f"class {name}(TypedDict):")
    print(f'    """')
    print(f"    {description}")
    print(f'    """')
    for n, p in properties.items():
        prop_type = property_type(n, p, enums)
        print(f"    {n}: {prop_type}")
    print()


def emit_enum(name, values):
    print(f"{name} = Union[")
    for v in values:
        print(f'    Literal["{v}"],')
    print("]")
    print()


def property_type(n, p, enums):

    if "type" in p:
        t = p["type"]
        if t == "array":
            item_type = property_type(None, p["items"], enums)
            return f"List[{item_type}]"
        elif t == "object":
            if "additionalProperties" in p:
                value_type = property_type(None, p["additionalProperties"], enums)
                return f"Dict[str, {value_type}]"
            else:
                say(p)
        elif t == "number":
            return type_mapping[p["format"]]
        elif "enum" in p:
            return enums[tuple(p["enum"])]
        else:
            return type_mapping[p["type"]]

    elif "$ref" in p:
        return p["$ref"]

    else:
        raise Exception(json.dumps(p, indent=2))


@dataclass
class Param:
    name: str
    type: str
    location: str
    required: bool = False
    repeated: bool = False

    def __post_init__(self):
        if self.repeated:
            self.type = f"List[{self.type}]"


def emit_methods(resources, enums, base_url):

    for name, spec in resources.items():
        print(f"# {name}")
        for method_name, m in spec["methods"].items():

            ps = method_params(m, enums)

            args = [f"{snake_case(p.name)}: {p.type}" for p in ps]

            if req := m.get("request"):
                request_type = property_type(None, req, enums)
                args.append(f"request: {request_type}")

            resp = property_type(None, m["response"], enums)
            doc = m["description"]

            # Translate parameter names
            path_args = {p.name: f"{{{snake_case(p.name)}}}" for p in ps}
            path = m["path"].format(**path_args)

            http_method = m["httpMethod"].lower()
            payload = ", json=request" if http_method == "post" else ""

            query_params = [
                f'"{p.name}": {snake_case(p.name)}' for p in ps if p.location == "query"
            ]
            qp = f"{{{', '.join(query_params)}}}" if query_params else ""
            qp_arg = f", params=params" if query_params else ""

            print(f"def {snake_case(method_name)}({', '.join(args)}) -> {resp}:")
            print(f'    """')
            print(f"    {doc}")
            print(f'    """')
            print(f'    url = f"{base_url}{path}"')
            if qp:
                print(f"    params: Dict[str, Any] = {qp}")
            print(f"    return requests.{http_method}(url{qp_arg}{payload}).json()")
            print("\n")


def method_params(method, enums):
    parameters = method["parameters"]
    order = [p for p in method["parameterOrder"]]

    def p(name, spec):
        return Param(
            name,
            property_type(name, spec, enums),
            spec["location"],
            spec.get("required", False),
            spec.get("repeated", False),
        )

    return sorted(
        (p(name, spec) for name, spec in parameters.items()),
        key=lambda p: (safe_index(order, p.name, len(order)), p.name),
    )


snake_case_pattern = re.compile(r"[A-Z]+")


def snake_case(s):
    return snake_case_pattern.sub(lambda m: f"_{m.group(0).lower()}", s)


def safe_index(xs, x, default):
    try:
        return xs.index(x)
    except ValueError:
        return default


if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = json.load(f)

    schemas = data["schemas"]
    resources = data["resources"]
    base_url = data["baseUrl"]

    enums = enum_names(schemas)

    enum_type_names = set(enums.values())

    print(f"# Until Python 4.0 we need this to allow forward type refs")
    print(f"from __future__ import annotations")
    print(f"from typing import Any, Dict, List, Literal, TypedDict, Union")
    print(f"import re")
    print(f"import requests")
    print()

    emit_methods(resources, enums, base_url)

    for name, spec in schemas.items():
        assert spec["id"] == name
        assert spec["type"] == "object"

        if name in enum_type_names:
            raise Exception(f"Name collision between dict and enum: {name}")

        emit_typed_dict(spec, enums)

    for values, name in enums.items():
        emit_enum(name, values)
