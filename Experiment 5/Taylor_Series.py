from sympy import *
from rich.console import Console
from rich.table import Table
from rich import box

def taylor_series(function, x0, n):
    x = symbols('x')
    result = 0
    for i in range(n):
        result += (diff(function, a, i) * (x - a)**i).subs(a, x0) / factorial(i)
    return result

console = Console()
table = Table(show_header=True, show_lines=True, box = box.SQUARE_DOUBLE_HEAD)

x0 = 0 # the point around which the Taylor series needs to be computed, when x0 = 0; the TS is calculated from the origin
n = 8 # the number of terms in the Taylor series
a = symbols('a')

table.add_column('Sr No.', justify='center', vertical = 'middle')
table.add_column('Function', justify='center', vertical = 'middle')
table.add_column('Taylor Series', justify='center', vertical = 'middle')

table.add_row('1', 'sine', str(taylor_series(cos(a), x0, n)))
table.add_row('2', 'cosine', str(taylor_series(sin(a), x0, n)))
table.add_row('3', 'exponential', str(taylor_series(exp(a), x0, n)))

console.print(table)

'''
OUTPUT:
┌────────┬─────────────┬─────────────────────────────────────────────────────────────────────┐
│ Sr No. │  Function   │                            Taylor Series                            │
╞════════╪═════════════╪═════════════════════════════════════════════════════════════════════╡
│   1    │    sine     │                  -x**6/720 + x**4/24 - x**2/2 + 1                   │
├────────┼─────────────┼─────────────────────────────────────────────────────────────────────┤
│   2    │   cosine    │                 -x**7/5040 + x**5/120 - x**3/6 + x                  │
├────────┼─────────────┼─────────────────────────────────────────────────────────────────────┤
│   3    │ exponential │ x**7/5040 + x**6/720 + x**5/120 + x**4/24 + x**3/6 + x**2/2 + x + 1 │
└────────┴─────────────┴─────────────────────────────────────────────────────────────────────┘
'''