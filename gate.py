import sympy as sy
from utils import *
from QCIS_instr import QCIS_instr


class Gate:
    def __init__(self, n, mat, ctrl=0, instr=None):
        self.n = n
        self.matrix = sy.Matrix(mat)
        self.ctrl_num = ctrl

    def get_matrix(self, qubit_map, ctrl_map=None, n=0):
        if ctrl_map is None:
            ctrl_map = []
        qubit_map = list(qubit_map)
        ctrl_map = list(ctrl_map)

        if n == 0:
            n = self.n

        if self.ctrl_num == 0:
            if not qubit_map:
                return self.matrix
        else:
            if ctrl_map == [] and qubit_map == []:
                return self.matrix

        res = sy.ones(2 ** n, 2 ** n)

        matI = sy.eye(2)

        for p in range(n):
            if p not in qubit_map:
                mark = get_mark([p], n)
                addr = gen_subset(mark)
                for i in range(matI.rows):
                    for j in range(matI.cols):
                        for si in addr:
                            mi = map_bit(i, si, [p])
                            for sj in addr:
                                mj = map_bit(j, sj, [p])
                                res[mi, mj] = res[mi, mj] * matI[i, j]

        mark = get_mark(qubit_map, n)
        ctrl_mark = get_mark(ctrl_map, 0)
        addr = gen_subset(mark)

        for i in range(self.matrix.rows):
            for j in range(self.matrix.cols):
                for si in addr:
                    mi = map_bit(i, si, qubit_map)
                    for sj in addr:
                        mj = map_bit(j, sj, qubit_map)
                        if ctrl_map:
                            if mi & ctrl_mark and mj & ctrl_mark:
                                res[mi, mj] = res[mi, mj] * self.matrix[i, j]
                            else:
                                res[mi, mj] = res[mi, mj] * (i == j)
                        else:
                            res[mi, mj] = res[mi, mj] * self.matrix[i, j]
        return res


class Circuit:
    def __init__(self, n):
        self.n = n
        self.gates = []
        self.matrix = sy.eye(2 ** n)

    def add_gates(self, gates: list, init=0):
        pass

    @staticmethod
    def make_from_gates_sequence(gates_sequence: list, n=0):
        pass

    @staticmethod
    def combine_gates(gates: list, n):
        pass
