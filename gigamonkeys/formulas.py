from __future__ import annotations

import re
from dataclasses import dataclass
from functools import singledispatch
from typing import Any
from typing import Tuple

from gigamonkeys.ast import AST
from gigamonkeys.ast import BinaryOp
from gigamonkeys.ast import UnaryOp

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Formulaic:
    def to_formula(self, sheet=None):
        pass


@singledispatch
def formula(arg, sheet):
    return repr(arg)


@formula.register
def formula_Formulaic(arg: Formulaic, sheet):
    return arg.to_formula(sheet)


@formula.register
def formula_str(arg: str, sheet):
    return arg


@formula.register
def formula_bool(arg: bool, sheet):
    return str(arg).upper()


@formula.register
def formula_BinaryOp(arg: BinaryOp, sheet=None):
    return f"({formula(arg.left, sheet)} {arg.op} {formula(arg.right, sheet)})"


@formula.register
def formula_UnaryOp(arg: UnaryOp, sheet=None):
    return f"({arg.op} {formula(arg.value, sheet)})"


@dataclass
class Function(AST, Formulaic):

    function: str
    args: Tuple[Any, ...]

    def to_formula(self, sheet=None):
        return f"{self.function}({', '.join(formula(a, sheet) for a in self.args)})"


@dataclass
class Cell(AST, Formulaic):

    "A cell in a spreadsheet."
    sheet: str
    col: str
    row: int

    def next_row(self, n=1):
        return Cell(self.sheet, self.col, self.row + n)

    def prev_row(self, n=1):
        return self.next_row(-n)

    def to_formula(self, sheet=None):
        "Render for use on the given sheet."
        if sheet == self.sheet:
            return f"{self.col}{self.row}"
        else:
            return f"{self.sheet}!{self.col}{self.row}"


@dataclass
class Range(Formulaic):

    top_left: Cell
    bottom_right: Cell

    def to_formula(self, sheet=None):
        if sheet == self.top_left.sheet:
            return (
                f"{formula(self.top_left, self.top_left.sheet)}:{formula(self.bottom_right, self.bottom_right.sheet)}"
            )
        else:
            return f"{formula(self.top_left, None)}:{formula(self.bottom_right, self.bottom_right.sheet)}"


def cell(name: str, sheet=None):
    if m := re.match(r"^(?:(?:'(.*?)')|(.*?))!([A-Za-z]+)(\d+)$", name):
        return Cell(m.group(1) or m.group(2), m.group(3), int(m.group(4)))
    elif sheet and (m := re.match(r"^([A-Za-z]+)(\d+)$", name)):
        return Cell(sheet, m.group(1), int(m.group(2)))
    else:
        raise Exception(f"{name} not a legal cell name.")


def column_name(i: int) -> str:
    "Convert 0-based index to A, B, ... Z, AA, AB, ... column name."
    a, b = divmod(i, 26)
    return f"{column_name(a - 1) if a > 0 else ''}{alphabet[b]}"


def column_index(n: str) -> int:
    "Convert A, B, ... Z, AA, AB, ... column name to 0-based index."
    acc = 0
    for c in n:
        acc *= 26
        acc += alphabet.index(c) + 1
    return acc - 1
