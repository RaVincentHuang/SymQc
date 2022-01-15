from utils import *
import sympy
from gate import Gate, ParametersGate
from QCIS_instr import QCIS_instr, QCISOpCode
from gates_lib import lib_gate


class Qsim:
    def __init__(self, n):
        self.state = sympy.Matrix(sympy.symbols('a:' + "%d" % (1 << n)))
        self.qubits_num = n
        self.global_circuit = None

    def apply(self):
        pass

    def apply_instr(self, instr: QCIS_instr):
        if instr.op_code.is_single_qubit_op():
            gate = Gate(lib_gate(instr))
            qubit = int(instr.qubit[1:])
            self.apply_gate(gate, [qubit])
        elif instr.op_code.is_two_qubit_op():
            if instr.op_code == QCISOpCode.CNOT or instr.op_code == QCISOpCode.CZ:
                gate = Gate(lib_gate(instr), 1)
                qubit = int(instr.target_qubit[1:])
                ctrl = int(instr.control_qubit[1:])
                self.apply_gate(gate, [ctrl, qubit])
            else:
                gate = Gate(lib_gate(instr))
                qubit = int(instr.target_qubit[1:])
                fake_ctrl = int(instr.control_qubit[1:])
                self.apply_gate(gate, [qubit, fake_ctrl])
        elif instr.op_code.is_measure_op():
            gate = Gate(lib_gate(instr))
            qubit_list = [int(qubit[1:]) for qubit in instr.qubits_list]
            self.apply_gate(gate, qubit_list)

    def apply_gate(self, gate: Gate, target_qubits: list, parameters=None, extra_optional_control_qubits=None) \
            -> sympy.Matrix:

        if extra_optional_control_qubits is None:
            extra_optional_control_qubits = []
        if parameters is None:
            parameters = []
        if gate.ctrl_num != 0:
            qubit_map = target_qubits[gate.ctrl_num:]
            ctrl_map = target_qubits[0: gate.ctrl_num] + extra_optional_control_qubits
        else:
            qubit_map = target_qubits
            ctrl_map = [] + extra_optional_control_qubits

        if isinstance(gate, ParametersGate):
            G = gate.get_matrix(get_discrete(qubit_map), parameters=parameters)
        else:
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
                x = sympy.Matrix([self.state[i] for i in addrs])
                x = G * x
                for i, j in zip(addrs, x):
                    self.state[i] = j
        return self.state
