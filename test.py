import sympy
from kernel.utils import kron

x = sympy.Matrix(sympy.symbols('q1' + '_{(:2)}'))
print(sympy.latex(x))
sympy.pprint(x)
