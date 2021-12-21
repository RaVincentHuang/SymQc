import sympy
from utils import *
from gates import *


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
    f = lambda x:res
    return gate(n, f)

def combine(chain, n):

    vis = [0] * n
    mark = 0
    res = sympy.ones(2**n, 2**n)
    for g in chain:
        mark = 0
        for j in g.opt_list:
            vis[j] = 1
            mark |= 1 << j

        mark = (~mark) & ((1 << n) - 1)
        oplist = genSubset(mark)

        for i in range(g.gate.mat.rows):
            for j in range(g.gate.mat.cols):
                for si in oplist:
                    for sj in oplist:
                        mi = mapBit(i, si, g.opt_list)
                        mj = mapBit(j, sj, g.opt_list)
                        res[mi, mj] = res[mi, mj] * g.gate.mat[i, j]

    matI = sympy.eye(2)
    
    for p in range(len(vis)):
        if vis[p] == 0:
            mark = 1 << p
            mark = (~mark) & ((1 << n) - 1)
            oplist = genSubset(mark)
            for i in range(matI.rows):
                for j in range(matI.cols):
                    for si in oplist:
                        for sj in oplist:
                            mi = mapBit(i, si, [p])
                            mj = mapBit(j, sj, [p])
                            res[mi, mj] = res[mi, mj] * matI[i, j]
    f = lambda x:res
    return gate(n, f)