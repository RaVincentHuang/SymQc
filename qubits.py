import sympy
from gates_lib import I


class Q_state:
    def __init__(self, n=6):
        self.size = n
        self.exp = 1 << n
        s = "a:" + str(self.exp)
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
