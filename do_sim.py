from argparse import ArgumentParser
from pathlib import Path
from my_parser import QCISParser


def compiler(_prog):
    _parser = QCISParser()
    success, instructions, names = _parser.parse(data=_prog)
    if not success:
        print(_parser.error_list)
        raise ValueError(
            "QCIS parser failed to compile the given QCIS program.")

    print(instructions, names)


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

print(prog)

compiler(prog)



