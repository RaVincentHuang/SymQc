from kernel.ket.state import State
from sympy import pprint

s = State(["q1", "q2", "q3", "q4", "q6"])

s.merge("q1", "q3")

s.merge("q2", "q4")

s.merge("q1", "q2")

pprint(s.tensor[0].ket)
