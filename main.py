from kernel import *
import sympy as sy
from sympy import pprint
from utils import *
from gates import *
from qubits import *

a = sy.symbols('a:2:2')
A = Matrix([[a[0],a[1]],[a[2],a[3]]])

b = sy.symbols('b:2:2')
B = Matrix([[b[0],b[1]],[b[2],b[3]]])

d = sy.symbols('d:2:2')
D = Matrix([[d[0],d[1]],[d[2],d[3]]])

c = sy.symbols('c:4:4')
C = Matrix([[c[0],c[1], c[2],c[3]], [c[4], c[5], c[6], c[7]], [c[8], c[9], c[10], c[11]], [c[12], c[13], c[14], c[15]]])


x = gate(1, X)
x.mat = A

y = gate(1, Y)
y.mat = B

z = gate(1, Z)
z.mat = D

cnot = gate(2, CNOT)
cnot.mat = C

cx = gate(1, X)
x.mat = A
xx = gate_call(x, [0], [1])


# CX = combine([xx], 2)
# print("CX")
# pprint(CX.mat)

xx = gate_call(x, [0])
yy = gate_call(y, [1])
x0 = make_U([xx], 2)
y0 = make_U([yy], 2)
xy = make_U([xx, yy], 2)

xx = gate_call(x, [1])
yy = gate_call(y, [0])
yx = make_U([yy, xx ], 2)

# print("x")
# pprint(x0.mat)
# print("y")
# pprint(y0.mat)
print("xy")
pprint(xy.mat)
print("yx")
pprint(yx.mat)
# pprint(x0.mat * y0.mat)

# print("xy")
# pprint(xy.mat)

# xy0 = make_U([xx, yy], 3)
# print("xy0")
# pprint(xy0.mat)

# xx = gate_call(x, [0])
# yy = gate_call(y, [2])
# zz = gate_call(z, [1])
# x0y = make_U([xx, yy], 3)
# xzy = make_U([xx, zz, yy], 3)

# print("x0y")
# pprint(x0y.mat)

# print("xzy")
# pprint(xzy.mat)


# X0Y = combine([xx, yy], 3)
# print("X0Y")
# pprint(X0Y.mat)

# XZY = combine([xx, zz, yy], 3)
# pprint(XZY.mat)

# ccnot = gate_call(cnot, [1,2])

# print("reday")
# make_U([yy, xx], 3)

# print(XZY.mat == xzy.mat)
# print(X0Y.mat == x0y.mat)

"""

⎡a₀₀⋅b₀₀  a₀₁⋅b₀₀  a₀₀⋅b₀₁  a₀₁⋅b₀₁⎤
⎢                                  ⎥
⎢a₁₀⋅b₀₀  a₁₁⋅b₀₀  a₁₀⋅b₀₁  a₁₁⋅b₀₁⎥
⎢                                  ⎥
⎢a₀₀⋅b₁₀  a₀₁⋅b₁₀  a₀₀⋅b₁₁  a₀₁⋅b₁₁⎥
⎢                                  ⎥
⎣a₁₀⋅b₁₀  a₁₁⋅b₁₀  a₁₀⋅b₁₁  a₁₁⋅b₁₁⎦



⎡a₀₀⋅b₀₀  a₀₁⋅b₀₀     0        0     a₀₀⋅b₀₁  a₀₁⋅b₀₁     0        0   ⎤
⎢                                                                      ⎥
⎢a₁₀⋅b₀₀  a₁₁⋅b₀₀     0        0     a₁₀⋅b₀₁  a₁₁⋅b₀₁     0        0   ⎥
⎢                                                                      ⎥
⎢   0        0     a₀₀⋅b₀₀  a₀₁⋅b₀₀     0        0     a₀₀⋅b₀₁  a₀₁⋅b₀₁⎥
⎢                                                                      ⎥
⎢   0        0     a₁₀⋅b₀₀  a₁₁⋅b₀₀     0        0     a₁₀⋅b₀₁  a₁₁⋅b₀₁⎥
⎢                                                                      ⎥
⎢a₀₀⋅b₁₀  a₀₁⋅b₁₀     0        0     a₀₀⋅b₁₁  a₀₁⋅b₁₁     0        0   ⎥
⎢                                                                      ⎥
⎢a₁₀⋅b₁₀  a₁₁⋅b₁₀     0        0     a₁₀⋅b₁₁  a₁₁⋅b₁₁     0        0   ⎥
⎢                                                                      ⎥
⎢   0        0     a₀₀⋅b₁₀  a₀₁⋅b₁₀     0        0     a₀₀⋅b₁₁  a₀₁⋅b₁₁⎥
⎢                                                                      ⎥
⎣   0        0     a₁₀⋅b₁₀  a₁₁⋅b₁₀     0        0     a₁₀⋅b₁₁  a₁₁⋅b₁₁⎦

"""
# Q = Q_state(2)

# g = [gate_call(gate(1, lib_call("X")), [0]), gate_call(gate(1, lib_call("Y")), [1]),
#      gate_call(gate(1, lib_call("Z")), [2]), gate_call(gate(1, lib_call("H")), [3]),
#      gate_call(gate(2, lib_call("CNOT")), [4, 5])]

# A = [gate_call(gate(1, lib_call("X")), [0])]
# B = [gate_call(gate(1, lib_call("Y")), [1])]
# C = [gate_call(gate(1, lib_call("X")), [0]), gate_call(gate(1, lib_call("Y")), [1])]
# # sympy.pprint(make_U(A, 2).mat * make_U(B, 2).mat)
# # sympy.pprint(make_U(C, 2).mat)
# sympy.pprint(Q.state)
# X = gate_call(gate(2, lib_call("CZ")), [0, 1])
# Q = do_mul(Q, X)
# X = gate_call(gate(2, lib_call("CZ")), [0, 1])
# sympy.pprint(Q.state)


# Q.state = make_U(g, 6).mat * Q.state
# print(Q.state)
# print("============================================================")
# g = []
# g.append(gate_call(gate(1, lib_call("S")), [0]))
# g.append(gate_call(gate(1, lib_call("T")), [1]))
# g.append(gate_call(gate(2, lib_call("SWAP")), [2, 3]))
# g.append(gate_call(gate(2, lib_call("CZ")), [4, 5]))
#
# Q.state = make_U(g, 6).mat * Q.state
# sympy.pprint(Q.state)
# sympy.pprint(make_U(g, 6).mat)

# 不同gate的实现
"""
class sim:
    def __init__(self):
        self.Q =
        self.G_n =
        self.circuit_global = circuit()


    def apply(self):
        pass

class gate:
    def __init__(self):
        self.num_qubits = None
        self.mat = None
        self.ctrl_num = None
        self.name = ""
    def get_matrix(self):
        pass



class circuit:
    def __init__(self):
        self.qubit_list = []
        self.gate_list = []

while True:
    sim.do(X, [0])
    sim.do(Y, [1])
    sim.Y()
    sim.X()
"""