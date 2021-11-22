import sympy
from gates import *


class Q_state:
    def __init__(self, n=6):
        self.size = n
        exp = 1 << n
        s = "a:" + str(exp)
        self.state = sympy.symbols(s)


class gate:
    def __init__(self, opt=1, est=I):
        self.opt = opt
        exp = 1 << opt
        self.mat = est(exp)


class gate_type:
    def __init__(self, g: gate, s: list):
        self.opt = g.opt
        self.opt_list = []
        for i in range(self.opt):
            self.opt_list.append(s[i])


def make_U(n, chain: list):
    pass