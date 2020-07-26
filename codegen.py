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


def walk_type(parent, property_name, p, fn):
    if "type" in p:
        t = p["type"]
        if t == "array":
            yield from walk_type(parent, property_name, p["items"], fn)
        else:
            yield from fn(parent, property_name, p)


def walk_properties(schemas, fn):
    for name, spec in schemas.items():
        properties = spec["properties"]
        for n, p in properties.items():
            yield from walk_type(name, n, p, fn)


def walk_parameters(resources, fn):
    def walk_methods(resource):
        for method_name, method in resource["methods"].items():
            for name, spec in method["parameters"].items():
                yield from walk_type(method_name, name, spec, fn)

        for sub_resource in resource.get("resources", {}).values():
            yield from walk_methods(sub_resource)

    for resource in resources.values():
        yield from walk_methods(resource)


def enum_names(schemas, resources):
    def enum_values(parent, key, p):
        if "enum" in p:
            yield (parent, key, tuple(p["enum"]))

    enums = defaultdict(list)
    for parent, key, values in walk_properties(schemas, enum_values):
        enums[values].append((parent, key))

    for parent, key, values in walk_parameters(resources, enum_values):
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
        prop_type = translate_type(n, p, enums)
        print(f"    {n}: {prop_type}")
    print()


def emit_enum(name, values):
    print(f"{name} = Union[")
    for v in values:
        print(f'    Literal["{v}"],')
    print("]")
    print()


def translate_type(n, p, enums):

    if "type" in p:
        t = p["type"]
        if t == "array":
            item_type = translate_type(None, p["items"], enums)
            return f"List[{item_type}]"
        elif t == "object":
            if "additionalProperties" in p:
                value_type = translate_type(None, p["additionalProperties"], enums)
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


def emit_resources(resources, enums, base_url, indent=0):

    indentation = " " * (indent * 4)

    def emit(x=None):
        if x is not None:
            print(f"{indentation}{x}")
        else:
            print()

    for name, spec in resources.items():

        if indent == 0:
            emit(f"def {name}():")
            emit(f"    token = login(scopes).token")
            emit(f'    headers = {{"Authorization": f"Bearer {{token}}"}}')
            emit(f"    return _{name}(headers)")
        else:
            emit(f"def {name}(self):")
            emit(f"    return self._{name}(self.headers)")
        emit()
        emit()
        emit(f"class _{name}:")
        emit()
        emit(f"    def __init__(self, headers):")
        emit(f"        self.headers = headers")
        emit()

        for method_name, m in spec["methods"].items():

            ps = method_params(m, enums)

            args = [f"{snake_case(p.name)}: {p.type}" for p in ps]

            if req := m.get("request"):
                request_type = translate_type(None, req, enums)
                args.append(f"request: {request_type}")

            resp = translate_type(None, m["response"], enums)
            doc = m["description"]

            # Translate parameter names
            path_args = {p.name: f"{{{snake_case(p.name)}}}" for p in ps}
            path = m["path"].format(**path_args)

            http_method = m["httpMethod"].lower()
            payload = ", json=request" if http_method == "post" else ""

            query_params = [f'"{p.name}": {snake_case(p.name)}' for p in ps if p.location == "query"]
            qp = f"{{{', '.join(query_params)}}}" if query_params else ""
            qp_arg = f", params=params" if query_params else ""

            emit(f"    def {snake_case(method_name)}(self, {', '.join(args)}) -> {resp}:")
            emit(f'         """')
            emit(f"        {doc}")
            emit(f'         """')
            emit(f'         url = f"{base_url}{path}"')
            if qp:
                emit(f"         params: Dict[str, Any] = {qp}")
            emit(f"         return requests.{http_method}(url{qp_arg}{payload}, headers=self.headers).json()")
            emit()
            emit()

        if sub_resources := spec.get("resources"):
            emit_resources(sub_resources, enums, base_url, indent=indent + 1)


def method_params(method, enums):
    parameters = method["parameters"]
    order = [p for p in method["parameterOrder"]]

    def p(name, spec):
        return Param(
            name,
            translate_type(name, spec, enums),
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
    scopes = list(data["auth"]["oauth2"]["scopes"].keys())

    enums = enum_names(schemas, resources)

    enum_type_names = set(enums.values())

    print(f"# Until Python 4.0 we need this to allow forward type refs")
    print(f"from __future__ import annotations")
    print(f"from typing import Any, Dict, List, Literal, TypedDict, Union")
    print(f"import re")
    print(f"import requests")
    print(f"from login import login")
    print()
    print(f"scopes = {scopes}")

    emit_resources(resources, enums, base_url)

    for name, spec in schemas.items():
        assert spec["id"] == name
        assert spec["type"] == "object"

        if name in enum_type_names:
            raise Exception(f"Name collision between dict and enum: {name}")

        emit_typed_dict(spec, enums)

    for values, name in enums.items():
        emit_enum(name, values)
