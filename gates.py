import sympy
from sympy.physics.matrices import msigma

# table = {"I" : I, "X" : X, "Y" : Y, "Z" : Z, "H" : H, "CNOT" : CONT}

def I(n = 2):
    return sympy.eye(n)


def X(n = 0):
    return msigma(1)


def Y(n = 0):
    return msigma(2)


def Z(n = 0):
    return msigma(3)


def H(n = 0):
    return 1 / sympy.sqrt(2) * (sympy.Matrix([[1, 1], [1, -1]]))


def CNOT(n = 0):
    return sympy.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

