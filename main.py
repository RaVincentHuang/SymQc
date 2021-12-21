from kernel import *

Q = Q_state(2)

g = [gate_call(gate(1, lib_call("X")), [0]), gate_call(gate(1, lib_call("Y")), [1]),
     gate_call(gate(1, lib_call("Z")), [2]), gate_call(gate(1, lib_call("H")), [3]),
     gate_call(gate(2, lib_call("CNOT")), [4, 5])]

A = [gate_call(gate(1, lib_call("X")), [0])]
B = [gate_call(gate(1, lib_call("Y")), [1])]
C = [gate_call(gate(1, lib_call("X")), [0]), gate_call(gate(1, lib_call("Y")), [1])]
# sympy.pprint(make_U(A, 2).mat * make_U(B, 2).mat)
# sympy.pprint(make_U(C, 2).mat)
sympy.pprint(Q.state)
X = gate_call(gate(2, lib_call("CZ")), [0, 1])
Q = do_mul(Q, X)
X = gate_call(gate(2, lib_call("CZ")), [0, 1])
sympy.pprint(Q.state)


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
