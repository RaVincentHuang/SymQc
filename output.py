import os
from sympy import Matrix, latex
from gate import Gate
from QCIS_instr import QCIS_instr, QCISOpCode
from kernel import Qsim


class store:
    def __init__(self, init: Qsim):
        self.instr_save = []
        self.state_save = []
        self.circuit_save = []
        self.gate_save = []
        self.init_state = init.state.copy()

    def save_instr(self, state: Matrix, instr: QCIS_instr, gate: Gate):
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
        self.state_save.append(state.copy())
        self.gate_save.append(gate)

    def output_list(self, instr_list: list, qcis_name="test.qcis", name='a.md'):
        file = open(name, 'w')
        file.write("# The ans of %s\n\n" % qcis_name)
        file.write("**Init state** is: \n$$\n%s\n$$\n\n" % latex(self.init_state.transpose()))
        for i in range(len(self.instr_save)):
            file.write("```assembly\n%d. %s\n```\n\n" % (i + 1, self.instr_save[i]))
            if i in instr_list:
                file.write("$$\n%s\n$$\n" % latex(self.gate_save[i].matrix))
                file.write("$$\n%s\n$$\n" % latex(self.state_save[i].transpose()))
        file.write("**Final state** is: \n$$\n%s\n$$\n\n" % latex(self.state_save[-1].transpose()))
        file.close()

    def output_all(self, qcis_name="test.qcis", name='a.md'):
        file = open(name, 'w')
        file.write("# The ans of %s\n\n" % qcis_name)
        file.write("**Init state** is: \n$$\n%s\n$$\n\n" % latex(self.init_state.transpose()))
        for i in range(len(self.instr_save)):
            file.write("```assembly\n%d. %s\n```\n\n" % (i + 1, self.instr_save[i]))
            file.write("$$\n%s\n$$\n" % latex(self.gate_save[i].matrix))
            file.write("$$\n%s\n$$\n" % latex(self.state_save[i].transpose()))
        file.write("**Final state** is: \n$$\n%s\n$$\n\n" % latex(self.state_save[-1].transpose()))
        file.close()



