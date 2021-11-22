import sympy
from utils import *
from gates import *
from qbits import *

x = gate(1, X)
y = gate(1, Y)
cnot = gate(2, CNOT)

xx = gate_call(x, [2])
yy = gate_call(y, [0])
ccnot = gate_call(cnot, [1,2])

print("reday")
make_U([yy, xx], 3)