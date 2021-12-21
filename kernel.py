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
    if len(g.opt_list) == 1:
        t = g.opt_list[0]
        sec = 1 << t
        U = g.gate
        for u in range(0, state.exp // sec, 2):
            for v in range(sec):
                idx = u * sec + v
                state.state[idx], state.state[idx + sec] = U * sympy.Matrix([state.state[idx], state.state[idx + sec]])
    else:
        t, a = g.opt_list[0], g.opt_list[1]
        ctrl = 1 << a
        sec = 1 << t
        U = g.gate.mat
        idx = 0
        for _ in range(state.exp // 4):
            if (idx >> t) & 0b1 == 1:
                idx += sec
            if (idx >> a) & 0b1 == 0:
                idx += ctrl
            state.state[idx], state.state[idx + sec] = U * sympy.Matrix([state.state[idx], state.state[idx + sec]])
            idx += 1
    return state



