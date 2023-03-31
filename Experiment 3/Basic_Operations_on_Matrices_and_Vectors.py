import numpy as np
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
table = Table(show_header=True, show_lines=True, box = box.SQUARE_DOUBLE_HEAD)

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 4], [6, 8]])
C = np.array([[4, 9], [16, 25]])

table.add_column('Sr No.', justify="center")
table.add_column('Operation', justify="left")
table.add_column('Result', justify="center")

table.add_row('1', 'Add', str(np.add(A, B)))
table.add_row('2', 'Subtract', str(np.subtract(A, B)))
table.add_row('3', 'Multiply', str(np.multiply(A, B)))
table.add_row('4', 'Divide', str(np.divide(B, A)))
table.add_row('5', 'Dot', str(np.dot(A, B)))
table.add_row('6', 'Sqrt', str(np.sqrt(C)))
table.add_row('7', 'Sum', str(np.sum(A)))
table.add_row('8', 'Sum X-axis', str(np.sum(A, axis = 1)))
table.add_row('9', 'Sum Y-axis', str(np.sum(A, axis = 0)))
table.add_row('10', 'Transpose', str(A.T))
table.add_row('11', 'Max', str(np.max(A)))
table.add_row('12', 'Min', str(np.min(A)))
table.add_row('13', 'Mean', str(np.mean(A)))
table.add_row('14', 'Variance', str(np.var(A)))
table.add_row('15', 'Std Deviation', str(round(np.std(A), 3)))
table.add_row('16', 'Inverse', str(np.linalg.inv(A)))
table.add_row('17', 'Rank', str(np.linalg.matrix_rank(A)))

console.print(table)