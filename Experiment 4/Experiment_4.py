import numpy as np

A = np.array([[1, 0, 2, -1],
              [3, 0, 0, 5],
              [2, 1, 4, -3],
              [1, 0, 5, 0]])

eigen_values, eigen_vectors = np.linalg.eig(A)

print('Determinant : ', round(np.linalg.det(A), 2))
print('Trace : ', A.trace())
print('Eigen Values : ', eigen_values)
print('Eigen Vectors : ', eigen_vectors)