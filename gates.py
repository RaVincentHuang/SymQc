import sympy
from sympy.physics.matrices import msigma


def I(n):
    return sympy.eye(n)


def X(n):
    return msigma(1)


def Y(n):
    return msigma(2)


def Z(n):
    return msigma(3)


def H(n):
    return 1 / sympy.sqrt(2) * (sympy.Matrix([[1, 1], [1, -1]]))


def CONT(n):
    return sympy.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

