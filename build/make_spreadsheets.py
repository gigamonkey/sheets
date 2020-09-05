#!/usr/bin/env python

import json
import re
import sys
import textwrap
from collections import Counter
from collections import defaultdict
from dataclasses import dataclass
from typing import Any

type_mapping = {
    "any": "Any",
    "boolean": "bool",
    "double": "float",
    "float": "float",
    "integer": "int",
    "string": "str",
}

defaults_for_type = {
    "Any": "None",
    "bool": "False",
    "float": "0.0",
    "int": "0",
    "str": "",
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


def emit_typed_dict(spec, enums, total, optional):
    name = spec["id"]
    doc = spec["description"]
    properties = spec["properties"]

    print(f"class {name}(TypedDict{'' if total else ', total=False'}):")
    emit_docs(doc, 4)
    for n, p in properties.items():
        prop_type = translate_type(n, p, enums)
        if optional.get(n):
            prop_type = f"Optional[{prop_type}]"
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
        elif "enum" in p:
            return enums[tuple(p["enum"])]
        elif t == "number":
            return type_mapping[p["format"]]
        else:
            return type_mapping[p["type"]]

    elif "$ref" in p:
        return p["$ref"]

    else:
        raise Exception(json.dumps(p, indent=2))


def default_for_type(param_spec, enums):

    if param_spec.get("repeated"):
        return "None"
    elif "type" in param_spec:
        t = param_spec["type"]
        if t == "array":
            return "[]"
        elif t == "object":
            return "{}"
        elif "enum" in param_spec:
            return f'"{param_spec["enum"][0]}"'
        elif t == "number":
            return defaults_for_type[type_mapping[param_spec["format"]]]
        else:
            return defaults_for_type[type_mapping[t]]

    elif "$ref" in param_spec:
        return "None"

    else:
        raise Exception(json.dumps(p, indent=2))


@dataclass
class Param:
    name: str
    type: str
    location: str
    required: bool
    repeated: bool
    default: Any

    def __post_init__(self):
        if self.repeated:
            self.type = f"List[{self.type}]"

    def to_code(self, enums):
        snake_case(self.name)
        default = "" if self.required else f" = {self.default}"
        return f"{snake_case(self.name)}: {self.type}{default}"


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

            args = ", ".join(p.to_code(enums) for p in ps)

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

            emit(f"    def {snake_case(method_name)}(self, {args}) -> {resp}:")
            emit_docs(doc, (indent * 4) + 8)
            emit(f'        url = f"{base_url}{path}"')
            if qp:
                emit(f"        params: Dict[str, Any] = {qp}")
            emit(f"        return requests.{http_method}(url{qp_arg}{payload}, headers=self.headers).json()")
            emit()
            emit()

        if sub_resources := spec.get("resources"):
            emit_resources(sub_resources, enums, base_url, indent=indent + 1)


def emit_docs(doc, indent):
    doc = doc.strip()
    indentation = " " * indent
    if len(doc.splitlines()) > 1 or len(doc) > 80:
        print(f'{indentation}"""')
        for p in paragraphs(doc):
            print(textwrap.indent(textwrap.fill(p, 80), indentation))
        print(f'{indentation}"""')
    elif '"' in doc:
        print(f'{indentation}"""{doc}"""')
    else:
        print(f'{indentation}"{doc}"')


def paragraphs(text):
    lines = [s.strip() for s in text.splitlines()]
    ps = []
    buf = None
    for line in lines:
        if line:
            buf = f"{buf} {line}" if buf else line
        else:
            ps.append(buf)
            buf = ""
    if buf:
        ps.append(buf)
    return ps


def method_params(method, enums):

    parameters = method["parameters"]
    order = [p for p in method["parameterOrder"]]

    if req := method.get("request"):
        parameters["request"] = {
            "$ref": req["$ref"],
            "required": True,
            "location": None,
        }
        order.append("request")

    def p(name, spec):
        return Param(
            name,
            translate_type(name, spec, enums),
            spec["location"],
            spec.get("required", False),
            spec.get("repeated", False),
            default_for_type(spec, enums),
        )

    def sort_key(p):
        return (safe_index(order, p.name, len(order)), p.name)

    return sorted((p(name, spec) for name, spec in parameters.items()), key=sort_key)


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

    with open(sys.argv[2]) as f:
        extra = json.load(f)

    schemas = data["schemas"]
    resources = data["resources"]
    base_url = data["baseUrl"]
    scopes = list(data["auth"]["oauth2"]["scopes"].keys())

    enums = enum_names(schemas, resources)

    enum_type_names = set(enums.values())
    non_total = set(extra["non_total"])

    print(f"# Until Python 4.0 we need this to allow forward type refs")
    print(f"from __future__ import annotations")
    print(f"from typing import Any, Dict, List, Literal, Optional, TypedDict, Union")
    print(f"import re")
    print(f"import requests")
    print(f"from login import login")
    print()
    print(f"scopes = [")
    for s in scopes:
        print(f"    {s!r},")
    print("]")
    print()

    emit_resources(resources, enums, base_url)

    for name, spec in schemas.items():
        assert spec["id"] == name
        assert spec["type"] == "object"

        if name in enum_type_names:
            raise Exception(f"Name collision between dict and enum: {name}")

        emit_typed_dict(spec, enums, name not in non_total, extra["optional"].get(name, {}))

    for values, name in enums.items():
        emit_enum(name, values)
