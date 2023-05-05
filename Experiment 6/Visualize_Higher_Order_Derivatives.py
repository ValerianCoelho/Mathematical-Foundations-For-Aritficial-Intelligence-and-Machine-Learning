import matplotlib.pyplot as plt
from sympy import *

a = symbols('x')
function = cos(a)

function_Values = [diff(function, a, 1).subs(a, (deg*pi)/180) for deg in range(0, 720)]

plt.plot(function_Values)
plt.show()