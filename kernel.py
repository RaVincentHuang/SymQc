from utils import *
import sympy as sy
from gate import Gate
from QCIS_instr import QCIS_instr, QCISOpCode
from gates_lib import lib_gate


class Qsim:
    def __init__(self, n):
        self.state = sy.Matrix(sy.symbols('a:' + "%d" % (1 << n)))
        self.qubits_num = n
        self.global_circuit = None

    def apply(self):
        pass

    def apply_instr(self, instr: QCIS_instr):
        if instr.op_code.is_single_qubit_op():
            gate = Gate(1, lib_gate(instr))
            qubit = int(instr.qubit[1:])
            self.apply_gate(gate, [qubit])
        elif instr.op_code.is_two_qubit_op():
            if instr.op_code == QCISOpCode.CNOT or instr.op_code == QCISOpCode.CZ:
                gate = Gate(1, lib_gate(instr), 1)
                qubit = int(instr.target_qubit[1:])
                ctrl = int(instr.control_qubit[1:])
                self.apply_gate(gate, [qubit], [ctrl])
            else:
                gate = Gate(2, lib_gate(instr))
                qubit = int(instr.target_qubit[1:])
                ctrl = int(instr.control_qubit[1:])
                self.apply_gate(gate, [qubit, ctrl])
        elif instr.op_code.is_measure_op():
            gate = Gate(1, lib_gate(instr))
            qubit_list = [int(qubit[1:]) for qubit in instr.qubits_list]
            self.apply_gate(gate, qubit_list)

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


class Circuit:
    def __init__(self, n):
        self.n = n
        self.gates = []
        self.matrix = sy.eye(2 ** n)

    def add_gates(self, gates: list, init=0):
        pass

    @staticmethod
    def make_from_gates_sequence(gates_seqence: list, n=0):
        pass

    @staticmethod
    def combine_gates(gates: list, n):
        pass
