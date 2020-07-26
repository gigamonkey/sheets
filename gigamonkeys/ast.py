from dataclasses import dataclass
from typing import Any
from typing import List


class AST:

    "Mixin for bulding an AST using Python's operator overloading."

    # Binary ops

    def __add__(self, other):
        return BinaryOp("+", self, other)

    def __sub__(self, other):
        return BinaryOp("-", self, other)

    def __mul__(self, other):
        return BinaryOp("*", self, other)

    def __matmul__(self, other):
        return BinaryOp("@", self, other)

    def __truediv__(self, other):
        return BinaryOp("/", self, other)

    def __floordiv__(self, other):
        return BinaryOp("//", self, other)

    def __mod__(self, other):
        return BinaryOp("%", self, other)

    def __divmod__(self, other):
        return BinaryOp("divmod()", self, other)

    def __pow__(self, other, modulo=None):
        return BinaryOp("**", self, other)

    def __lshift__(self, other):
        return BinaryOp("<<", self, other)

    def __rshift__(self, other):
        return BinaryOp(">>", self, other)

    def __and__(self, other):
        return BinaryOp("&", self, other)

    def __xor__(self, other):
        return BinaryOp("^", self, other)

    def __or__(self, other):
        return BinaryOp("|", self, other)

    # Binary ops (reversed)

    def __radd__(self, other):
        return BinaryOp("+", other, self)

    def __rsub__(self, other):
        return BinaryOp("-", other, self)

    def __rmul__(self, other):
        return BinaryOp("*", other, self)

    def __rmatmul__(self, other):
        return BinaryOp("@", other, self)

    def __rtruediv__(self, other):
        return BinaryOp("/", other, self)

    def __rfloordiv__(self, other):
        return BinaryOp("//", other, self)

    def __rmod__(self, other):
        return BinaryOp("%", other, self)

    def __rdivmod__(self, other):
        return BinaryOp("divmod()", other, self)

    def __rpow__(self, other, modulo=None):
        return BinaryOp("**", other, self)

    def __rlshift__(self, other):
        return BinaryOp("<<", other, self)

    def __rrshift__(self, other):
        return BinaryOp(">>", other, self)

    def __rand__(self, other):
        return BinaryOp("&", other, self)

    def __rxor__(self, other):
        return BinaryOp("^", other, self)

    def __ror__(self, other):
        return BinaryOp("|", other, self)

    # Unary ops

    def __neg__(self):
        return UnaryOp("-", self)

    def __pos__(self):
        return UnaryOp("+", self)

    def __abs__(self):
        return UnaryOp("abs()", self)

    def __invert__(self):
        return UnaryOp("~", self)


@dataclass
class BinaryOp(AST):
    op: str
    left: Any
    right: Any


@dataclass
class UnaryOp(AST):

    op: str
    value: Any


@dataclass
class Value(AST):
    value: Any


@dataclass
class Function(AST):

    function: str
    args: List[Any]
