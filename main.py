from qubits import *

Q = Q_state(6)

g = [gate_call(gate(1, lib_call("X")), [0]), gate_call(gate(1, lib_call("Y")), [1]),
     gate_call(gate(1, lib_call("Z")), [2]), gate_call(gate(1, lib_call("H")), [3]),
     gate_call(gate(2, lib_call("CNOT")), [4, 5])]

A = [gate_call(gate(1, lib_call("X")), [0])]
B = [gate_call(gate(1, lib_call("Y")), [1])]
C = [gate_call(gate(1, lib_call("X")), [0]), gate_call(gate(1, lib_call("Y")), [1])]
sympy.pprint(make_U(A, 2).mat * make_U(B, 2).mat)
sympy.pprint(make_U(C, 2).mat)

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

