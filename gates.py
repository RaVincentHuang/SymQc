import sympy
from sympy.physics.matrices import msigma


def I(n=2):
    return sympy.eye(n)


def X(n=0):
    return msigma(1)


def Y(n=0):
    return msigma(2)


def Z(n=0):
    return msigma(3)


def H(n=0):
    return 1 / sympy.sqrt(2) * (sympy.Matrix([[1, 1], [1, -1]]))


def CNOT(n=0):
    return sympy.Matrix([[0, 1], [1, 0]])


def S(n=0):
    return sympy.Matrix([[1, 0], [0, sympy.I]])


def T(n=0):
    return sympy.Matrix([[1, 0], [0, sympy.exp(sympy.I * sympy.pi / 4)]])


def SWAP(n=0):
    return sympy.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])


def CZ(n=0):
    return sympy.Matrix([[1, 0], [0, -1]])


def CS(n=0):
    return sympy.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, sympy.I]])


table = {"I": I, "X": X, "Y": Y, "Z": Z, "H": H, "CNOT": CNOT, "S": S, "T": T, "SWAP": SWAP, "CZ": CZ, "CS": CS}


def lib_call(s: str):
    return table[s]


def my_call(mat: sympy.Matrix):
    return mat
