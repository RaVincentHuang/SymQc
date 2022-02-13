from argparse import ArgumentParser
from pathlib import Path
from QCIS.parser import QCISParser, QCISOpCode
from sympy import init_printing
from kernel.qubit import Qsim
from output.store import store
from output.symbol_map import symbol_map

"""
The main programme
"""


def compiler(_prog):
    """"""
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


# 1. Argument parsing
my_parser = ArgumentParser(description='QCIS simulator system based on symbolic operation')

my_parser.add_argument('input', type=str, help='the name of the input QCIS file')

my_parser.add_argument('-l', '--output_list', required=False, nargs='+', type=int, default=[],
                       help='the index of the instr we need the ans.')

my_parser.add_argument('-o', '--obj_name', required=False, type=str, default="a.md",
                       help='the filename of Markdown file.')

my_parser.add_argument('-N', required=False, type=int, help='the number of qubits in the symbolic simulator')

my_parser.add_argument("-s", "--symbol", help="use the symbol args", action="store_true")
args = my_parser.parse_args()

qcis_fn = Path(args.input).resolve()

if qcis_fn.suffix != '.qcis':
    raise ValueError(
        "Error: the input file name should end with the suffix '.qcis'.")

if not qcis_fn.exists():
    raise ValueError("cannot find the given file: {}".format(qcis_fn))

# 2. Read the QCIS file
prog = qcis_fn.open('r').read()

job_arr, max_q = compiler(prog)

if args.N is not None and args.N > max_q:
    max_q = args.N

# 3. Start simulating
Q = Qsim(max_q)
init_printing()
maps = symbol_map()

if args.symbol:
    for instr in job_arr:
        if instr.op_code == QCISOpCode.RXY:
            instr.altitude = maps.store_symbol("theta", instr.altitude)
            instr.azimuth = maps.store_symbol("phi", instr.azimuth)
        elif instr.op_code == QCISOpCode.XY or instr.op_code == QCISOpCode.XY2P or instr.op_code == QCISOpCode.XY2M:
            instr.azimuth = maps.store_symbol("phi", instr.azimuth)
        elif instr.op_code == QCISOpCode.RX or instr.op_code == QCISOpCode.RY or instr.op_code == QCISOpCode.RZ:
            instr.altitude = maps.store_symbol("theta", instr.altitude)


save = store(Q, maps, args.output_list)

idx = 1
for instr in job_arr:
    gate = Q.apply_instr(instr)

    if idx in save.out_list:
        save.save_instr(Q.state, instr, gate)

    idx += 1

save.output_markdown(args.input, args.obj_name)
