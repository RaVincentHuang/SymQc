from qubits import *
import sympy as sy
import cmath as cm

X = Gate(1, sy.Matrix([[0, 1],[1, 0]]))
Y = Gate(1, sy.Matrix([[0, -sy.I], [sy.I, 0]]))
Z = Gate(1, sy.Matrix([[1, 0], [0, -1]]))
H = Gate(1, sy.Matrix([[ 1/sy.sqrt(2),  1/sy.sqrt(2)], [ 1/sy.sqrt(2), - 1/sy.sqrt(2)]]))
S = Gate(1, sy.Matrix([[1, 0], [0, 1j]]))
T = Gate(1, sy.Matrix([[1, 0], [0, sy.E ** (sy.pi*sy.I/4)]]))

CNOT = Gate(1, sy.Matrix([[0, 1],[1, 0]]), 1)
CZ = Gate(1, sy.Matrix([[1, 0], [0, -1]]), 1)

Q = Qsim(2)
C = Circuit(4)
back = Q.state

# tmp = X.get_matrix([2], [], 4) * Q.state
Q.apply_gate(H, [1])
# sy.pprint(Q.state)
# sy.pprint(X.get_matrix([1], [], 2))
# sy.pprint(C.matrix)


# sy.pprint(tmp == Q.state)

# tmp = CNOT.get_matrix([1], [0], 4) * Q.state

Q.apply_gate(CNOT, [1], [0])
# sy.pprint(Q.state)
# sy.pprint(tmp)
# sy.pprint(tmp == Q.state)

# ttmp = C.matrix * back

# sy.pprint(ttmp == Q.state)
Q.apply_gate(T, [0])
sy.pprint(Q.state)

