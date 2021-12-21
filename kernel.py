import sympy
from utils import Kron
from qubits import gate, lib_call, gate_call, Q_state


def make_U(chain, n):
    seq = sorted(chain, key=lambda x: x.opt_list)

    now = 0
    res = sympy.eye(1)

    for g in seq:
        while g.opt_list[0] != now:
            res = Kron(lib_call("I")(2), res)
            now += 1
        res = Kron(g.gate.mat, res)
        now = g.opt_list[-1] + 1

    while now != n:
        res = Kron(lib_call("I")(2), res)
        now += 1

    return gate(n, lambda x: res)


def do_mul(state: Q_state, g: gate_call) -> Q_state:
    state
