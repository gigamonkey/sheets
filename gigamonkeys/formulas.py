from __future__ import annotations

import re
from dataclasses import dataclass
from functools import singledispatch

from gigamonkeys.ast import AST
from gigamonkeys.ast import BinaryOp
from gigamonkeys.ast import UnaryOp


class Formulaic:
    def to_formula(self, sheet=None):
        pass


@singledispatch
def formula(arg, sheet):
    return repr(arg)


@formula.register
def _(arg: Formulaic, sheet):
    return arg.to_formula(sheet)


@formula.register
def _(arg: str, sheet):
    return arg


@formula.register
def _(arg: bool, sheet):
    return str(arg).upper()


@formula.register
def _(arg: BinaryOp, sheet=None):
    return f"({formula(arg.left, sheet)} {arg.op} {formula(arg.right, sheet)})"


@formula.register
def _(arg: UnaryOp, sheet=None):
    return f"({arg.op} {formula(arg.value, sheet)})"


@dataclass
class Function(AST, Formulaic):

    function: str
    args: List[Any]

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
        return self.offset_row(-n)

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
