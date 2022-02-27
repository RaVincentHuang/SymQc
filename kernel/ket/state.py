from sympy import kronecker_product, Matrix, symbols
from kernel.utils import kron


class Qutensor:
    def __init__(self, qubit, vec):
        self.size = 1
        self.state = vec
        self.map = {qubit: 0}

    def insert_tensor(self, tensor):
        self.state = kron(self.state, tensor.state)
        for key in tensor.map.keys():
            tensor.map[key] += self.size
        self.size += tensor.size
        self.map.update(tensor.map)

    def insert_qubit(self, qubit, vec):
        self.map[qubit] = self.size
        self.size += 1
        self.state = kron(self.state, vec)


class State:
    def __init__(self, names):
        self.tensor = [Qutensor(qubit, Matrix(symbols(qubit + '_{(:2)}'))) for qubit in names]
        self.map = {}
        self.size = 0
        for qubit in names:
            self.map[qubit] = self.size
            self.size += 1

    def merge(self, qubit1, qubit2):
        tensor1, state1 = self.get_pos(qubit1)
        tensor2, state2 = self.get_pos(qubit2)

        if tensor1 == tensor2:
            return tensor1, state1, state2

        for key in self.tensor[tensor2].map.keys():
            self.map[key] = tensor1

        self.tensor[tensor1].insert_tensor(self.tensor[tensor2])
        self.tensor[tensor2] = None
        self.size -= 1

        return tensor1, self.tensor[tensor1].map[qubit1], self.tensor[tensor1].map[qubit2]

    def split(self, qubit1, qubit2):
        pass

    def judge(self, qubit1, qubit2):
        return False

    def get_pos(self, qubit):
        tensor = self.map[qubit]
        state = self.tensor[tensor].map[qubit]
        return tensor, state
