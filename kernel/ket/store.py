from output.store import store
from kernel.ket.state import State
from sympy import Matrix, latex, kronecker_product, symbols
from kernel.gate import Gate
from kernel.ket.qubit import Qsim_ket
from QCIS.instr import QCIS_instr, QCISOpCode
from output.symbol_map import symbol_map


class store_ket(store):
    def __init__(self, init: Qsim_ket, mapping: symbol_map, output_list):
        super().__init__(init, mapping, output_list)
        self.init_state = init.state

    def save_instr(self, state: State, instr: QCIS_instr, gate: Gate):
        ins_str = str(instr.op_code).removeprefix("QCISOpCode.")
        if instr.op_code.is_single_qubit_op():
            ins_str += '\t' + str(instr.qubit)
        elif instr.op_code.is_two_qubit_op():
            if instr.op_code == QCISOpCode.CNOT or instr.op_code == QCISOpCode.CZ:
                ins_str += '\t' + str(instr.control_qubit) + '\t' + str(instr.target_qubit)
            else:
                ins_str += '\t' + str(instr.control_qubit) + '\t' + str(instr.target_qubit)
        elif instr.op_code.is_measure_op():
            tmp = '\t'
            ins_str += '\t' + tmp.join([str(qubit) for qubit in instr.qubits_list])

        self.instr_save.append(ins_str)

        f = 1
        for tensor in state.tensor:
            if tensor:
                f *= (tensor.state.transpose() * tensor.ket)
        self.state_save.append(latex(f[0]))
        self.gate_save.append(latex(gate.matrix))

    def save_final(self, state: State):
        f = 1
        for tensor in state.tensor:
            if tensor:
                f *= (tensor.state.transpose() * tensor.ket)
        self.final_state = latex(f[0])

    def write_init(self):
        return self.init_state[0]



