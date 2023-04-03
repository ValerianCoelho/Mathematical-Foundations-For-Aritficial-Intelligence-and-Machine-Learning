import numpy as np
from rich.console import Console
from rich.table import Table
from rich import box

A = np.array([[1, 0, 2, -1],
              [3, 0, 0, 5],
              [2, 1, 4, -3],
              [1, 0, 5, 0]])

console = Console()
table = Table(show_header=True, show_lines=True, box = box.SQUARE_DOUBLE_HEAD)

table.add_column('Sr No.', justify='center', vertical = 'middle')
table.add_column('Operation', justify='center', vertical = 'middle')
table.add_column('Result', justify='center', vertical = 'middle')

eigen_values, eigen_vectors = np.linalg.eig(A)
U, s, V = np.linalg.svd(A, full_matrices=False)

table.add_row('1', 'Determinanat', str(round(np.linalg.det(A), 2)))
table.add_row('2', 'Trace', str(A.trace()))
table.add_row('3', 'Eigen Values', str(np.round(eigen_values, 1)))
table.add_row('4', 'Eigen Vectors', str(np.round(eigen_vectors, 1)))
table.add_row('5', 'U', str(np.round(U, 1)))
table.add_row('6', 's', str(np.round(s, 1)))
table.add_row('7', 'V', str(np.round(V, 1)))

console.print(table)

'''
OUTPUT:
┌────────┬───────────────┬─────────────────────────────────────────────┐
│ Sr No. │   Operation   │                   Result                    │
╞════════╪═══════════════╪═════════════════════════════════════════════╡
│   1    │ Determinanat  │                    30.0                     │
├────────┼───────────────┼─────────────────────────────────────────────┤
│   2    │     Trace     │                      5                      │
├────────┼───────────────┼─────────────────────────────────────────────┤
│   3    │ Eigen Values  │    [1.9+0.5j 1.9-0.5j 0.6+2.7j 0.6-2.7j]    │
├────────┼───────────────┼─────────────────────────────────────────────┤
│        │               │ [[-0.1+0.1j -0.1-0.1j -0.1+0.2j -0.1-0.2j]  │
│   4    │ Eigen Vectors │  [ 0.9+0.j   0.9-0.j   0.9+0.j   0.9-0.j ]  │
│        │               │  [ 0.2+0.j   0.2-0.j  -0.2+0.1j -0.2-0.1j]  │
│        │               │  [ 0.4+0.j   0.4-0.j   0.1+0.4j  0.1-0.4j]] │
├────────┼───────────────┼─────────────────────────────────────────────┤
│        │               │           [[-0.3  0.1  0.1 -0.9]            │
│   5    │       U       │            [ 0.2  0.9  0.3  0. ]            │
│        │               │            [-0.7 -0.   0.6  0.3]            │
│        │               │            [-0.6  0.3 -0.7  0.1]]           │
├────────┼───────────────┼─────────────────────────────────────────────┤
│   6    │       s       │              [7.6 5.9 1.9 0.3]              │
├────────┼───────────────┼─────────────────────────────────────────────┤
│        │               │           [[-0.2 -0.1 -0.8  0.5]            │
│   7    │       V       │            [ 0.5 -0.   0.3  0.8]            │
│        │               │            [ 0.8  0.3 -0.4 -0.4]            │
│        │               │            [-0.3  0.9  0.1  0.2]]           │
└────────┴───────────────┴─────────────────────────────────────────────┘
'''