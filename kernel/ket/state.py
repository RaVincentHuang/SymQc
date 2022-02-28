from sympy import Matrix, symbols

from kernel.utils import kron, make_ket


class Qutensor:
    def __init__(self, qubit, vec):
        self.size = 1
        self.state = vec
        self.map = {qubit: 0}
        self.ket = Matrix([symbols("\\ket{0_{%s}}" % qubit), symbols("\\ket{1_{%s}}" % qubit)])

    def insert_tensor(self, tensor):
        self.state = kron(self.state, tensor.state)
        for key in tensor.map.keys():
            tensor.map[key] += self.size
        self.size += tensor.size
        self.map.update(tensor.map)
        self.update_ket()

    def insert_qubit(self, qubit, vec):
        self.map[qubit] = self.size
        self.size += 1
        self.state = kron(self.state, vec)

    def update_ket(self):
        l = list(self.map.keys())
        x = make_ket(l)
        self.ket = Matrix([symbols("\\ket{%s}" % s) for s in x])


class State:
    def __init__(self, names):
        self.tensor = [Qutensor(qubit, Matrix([symbols("\\alpha_{%s}" % qubit), symbols("\\beta_{%s}" % qubit)])) for qubit
                       in names]
        self.size = len(names)
        self.map = dict([(qubit, i) for qubit, i in zip(names, range(self.size))])

    def merge(self, qubit1, qubit2):
        tensor1, state1 = self.get_pos(qubit1)
        tensor2, state2 = self.get_pos(qubit2)

        if tensor1 == tensor2:
            return tensor1, state1, state2

        if qubit1 < qubit2:
            for key in self.tensor[tensor2].map.keys():
                self.map[key] = tensor1

            self.tensor[tensor1].insert_tensor(self.tensor[tensor2])
            self.tensor[tensor2] = None
            self.size -= 1

            return tensor1, self.tensor[tensor1].map[qubit1], self.tensor[tensor1].map[qubit2]
        else:
            for key in self.tensor[tensor1].map.keys():
                self.map[key] = tensor2
            self.tensor[tensor2].insert_tensor(self.tensor[tensor1])
            self.tensor[tensor1] = None
            self.size -= 1

            return tensor2, self.tensor[tensor2].map[qubit1], self.tensor[tensor2].map[qubit2]

    def split(self, qubit1, qubit2):
        pass

    def judge(self, qubit1, qubit2):
        return False

    def get_pos(self, qubit):
        tensor = self.map[qubit]
        state = self.tensor[tensor].map[qubit]
        return tensor, state
