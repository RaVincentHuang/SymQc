import sympy as sy
from sympy import pprint
from utils import *
from gates import *
from qbits import *

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

xx = gate_call(x, [0])
yy = gate_call(y, [1])
x0 = make_U([xx], 2)
y0 = make_U([yy], 2)
xy = make_U([xx, yy], 2)
# print("x")
# pprint(x0.mat)
# print("y")
# pprint(y0.mat)
# print("xy")
# pprint(xy.mat)
# print("xy")
# pprint(x0.mat * y0.mat)

print("xy")
pprint(xy.mat)

xy0 = make_U([xx, yy], 3)
print("xy0")
pprint(xy0.mat)

xx = gate_call(x, [0])
yy = gate_call(y, [2])
zz = gate_call(z, [1])
x0y = make_U([xx, yy], 3)
xzy = make_U([xx, zz, yy], 3)

print("x0y")
pprint(x0y.mat)

print("xzy")
pprint(xzy.mat)


X0Y = combine([xx, yy], 3)
print("X0Y")
pprint(X0Y.mat)

XZY = combine([xx, zz, yy], 3)
pprint(XZY.mat)

ccnot = gate_call(cnot, [1,2])

print("reday")
make_U([yy, xx], 3)

print(XZY.mat == xzy.mat)
print(X0Y.mat == x0y.mat)

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