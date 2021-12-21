import sympy
from utils import *
from gates import *


class Q_state:
    def __init__(self, n=6):
        self.size = n
        exp = 1 << n
        s = "a:" + str(exp)
        self.state = sympy.Matrix(sympy.symbols(s))


class gate:
    def __init__(self, opt=1, est=I):
        self.opt = opt
        exp = 1 << opt
        self.mat = est(exp)


class gate_call:
    def __init__(self, g: gate, s: list):
        self.gate = g
        self.opt_list = s



def make_U(chain, n):
    seq = sorted(chain, key=lambda x: x.opt_list)

    now = 0
    res = sympy.eye(1)

    for g in seq:
        while g.opt_list[0] != now:
            res = Kron(I(2), res)
            now += 1
        res = Kron(g.gate.mat, res)
        now = g.opt_list[-1] + 1

    while now != n:
        res = Kron(I(2), res)
        now += 1

    return gate(n, lambda x: res)
