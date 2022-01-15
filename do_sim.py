from argparse import ArgumentParser
from pathlib import Path
from QCIS.parser import QCISParser
from sympy import init_printing
from kernel.qubit import Qsim
from output.output import store


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

my_parser.add_argument('-l', '--output_list', required=False, nargs='+', type=int,
                       help='the index of the instr we need the ans.')

my_parser.add_argument('-o', '--obj_name', required=False, type=str, default="a.md",
                       help='the filename of Markdown file.')

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
save = store(Q)


for instr in job_arr:
    save.save_instr(Q.state, instr, Q.apply_instr(instr))

if len(args.output_list):
    save.output_list(args.output_list, args.input, args.obj_name)
else:
    save.output_all(args.input, args.obj_name)
