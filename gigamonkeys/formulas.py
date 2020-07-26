from __future__ import annotations

import re
from ast import AST
from dataclasses import dataclass


@dataclass
class Cell(AST):

    "A cell in a spreadsheet."
    sheet: str
    col: str
    row: int

    def to_formula(self, sheet=None):
        "Render for use on the given sheet."
        if sheet == self.sheet:
            return f"{self.col}{self.row}"
        else:
            return f"{self.sheet}!{self.col}{self.row}"


@dataclass
class Range:

    top_left: Cell
    bottom_right: Cell

    def to_formula(self, sheet=None):
        if sheet == self.top_left.sheet:
            return f"{self.top_left.to_formula(self.top_left.sheet)}:{self.bottom_right.to_formula(self.bottom_right.sheet)}"
        else:
            return f"{self.top_left.to_formula()}:{self.bottom_right.to_formula(self.bottom_right.sheet)}"


def cell(name: str, sheet=None):
    if m := re.match(r"^(?:(?:'(.*?)')|(.*?))!([A-Za-z]+)(\d+)$", name):
        return Cell(m.group(1) or m.group(2), m.group(3), int(m.group(4)))
    elif sheet and (m := re.match(r"^([A-Za-z]+)(\d+)$", name)):
        return Cell(sheet, m.group(1), int(m.group(2)))
    else:
        raise Exception(f"{name} not a legal cell name.")


if __name__ == "__main__":

    print(cell("Sheet1!A1").to_formula())
    print(cell("A1", "'Another sheet'").to_formula("'Another sheet'"))

    r = Range(cell("Sheet1!A1"), cell("Sheet1!Z1000"))
    print(r.to_formula())
    print(r.to_formula("Sheet1"))
