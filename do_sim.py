from argparse import ArgumentParser
from pathlib import Path
from my_parser import QCISParser
from QCIS_instr import QCISOpCode
from sympy import pprint, init_printing, latex
from kernel import Qsim


def compiler(_prog):
    _parser = QCISParser()
    success, instructions, names = _parser.parse(data=_prog)
    if not success:
        print(_parser.error_list)
        raise ValueError(
            "QCIS parser failed to compile the given QCIS program.")

    max_qubit = 0
    for qubit in names:
        max_qubit = max(int(qubit[1:]), max_qubit)

    return instructions, max_qubit + 1


my_parser = ArgumentParser(description='QCIS simulator system based on symbolic operation')

my_parser.add_argument('input', type=str, help='the name of the input QCIS file')

my_parser.add_argument('-m', '--mode', required=False, type=str,
                       choices=['one_shot', 'final_state'],
                       help='the simulation mode used to simulate the given file.'
                            ' Default to one_shot.')

my_parser.add_argument('-n', '--num_shots', required=False, type=int, default=1,
                       help='the number of iterations performed in the `one_shot` mode.')

my_parser.add_argument('-N', required=False, type=int, help='the number of qubits in the symbolic simulator')

args = my_parser.parse_args()

qcis_fn = Path(args.input).resolve()

if qcis_fn.suffix != '.qcis':
    raise ValueError(
        "Error: the input file name should end with the suffix '.qcis'.")

if not qcis_fn.exists():
    raise ValueError("cannot find the given file: {}".format(qcis_fn))
prog = qcis_fn.open('r').read()

job_arr, max_q = compiler(prog)

if args.N is not None and args.N > max_q:
    max_q = args.N

Q = Qsim(max_q)
init_printing()


for instr in job_arr:
    print(instr.op_code)
    if instr.op_code == QCISOpCode.RXY:
        print("war")
    Q.apply_instr(instr)
    print("===============================")
    pprint(Q.state)
    print("===============================")
