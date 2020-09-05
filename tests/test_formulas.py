from gigamonkeys.formulas import *

c1 = cell("Sheet1!A1")
c2 = cell("A1", "'Another sheet'")
r = Range(cell("Sheet1!A1"), cell("Sheet1!Z1000"))

def test_no_sheet_specified():
    assert c1.to_formula() == "Sheet1!A1"

def test_no_sheet_specified_2():
    assert cell("A1", "Sheet1").to_formula() == "Sheet1!A1"

def test_on_different_sheet():
    assert c2.to_formula("Sheet1") == "'Another sheet'!A1"

def test_on_same_sheet():
    assert c2.to_formula("'Another sheet'") == "A1"

def test_range_no_sheet():
    assert r.to_formula() == "Sheet1!A1:Z1000"

def test_range_same_sheet():
    assert r.to_formula("Sheet1") == "A1:Z1000"

def test_range_different_sheet():
    assert r.to_formula("Another Sheet") == "Sheet1!A1:Z1000"

def test_function():
    assert Function("MAX", [r, c1, c1 + c2]).to_formula("Sheet1") == "MAX(A1:Z1000, A1, (A1 + 'Another sheet'!A1))"
