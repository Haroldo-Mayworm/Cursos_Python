import numpy as np

# Matriz inversa
matriz_a = np.array([[ 2,  5],
                     [ 1,  3]])

matriz_b = np.array([[ 3, -5],
                     [-1,  2]])

# print(np.linalg.inv(matriz_a))
# print(np.linalg.inv(matriz_b))

# print(matriz_a @ matriz_b)
# print(matriz_b @ matriz_a)


# Determinante
matriz_c = np.array([[ 1,  3,  2],
                     [ 4,  2,  4],
                     [ 3,  1,  5]])

print(np.linalg.det(matriz_c))

#
import scipy as sp
from scipy import linalg

print(sp.linalg.det(matriz_c))
