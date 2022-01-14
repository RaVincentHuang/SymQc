from utils import *
import sympy as sy
from gate import Gate
from QCIS_instr import QCIS_instr


class Qsim:
    def __init__(self, n):
        self.state = sy.Matrix(sy.symbols('a:' + "%d" % (1 << n)))
        self.qubits_num = n
        self.global_circuit = None

    def apply(self):
        pass

    def apply_instr(self, instr: QCIS_instr):
        if instr.op_code.is_single_qubit_op():
            self.apply_gate()

    def apply_gate(self, gate: Gate, qubit_map: list, ctrl_map=None) -> sy.Matrix:
        if ctrl_map is None:
            ctrl_map = []
        G = gate.get_matrix(get_discrete(qubit_map))
        qubit_map.sort()

        marki = get_mark(qubit_map, 0)
        mark = get_mark(qubit_map, self.qubits_num)

        ctrl_mark = get_mark(ctrl_map, 0)

        addr = gen_subset(mark)
        addri = sorted(gen_subset(marki))

        for s in addr:
            if ctrl_mark == 0 or s & ctrl_mark:
                addrs = [(s | i) for i in addri]
                x = sy.Matrix([self.state[i] for i in addrs])
                x = G * x
                for i, j in zip(addrs, x):
                    self.state[i] = j
        return self.state
