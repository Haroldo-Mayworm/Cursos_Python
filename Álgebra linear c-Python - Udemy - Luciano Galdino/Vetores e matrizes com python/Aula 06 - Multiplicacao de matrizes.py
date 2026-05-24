import numpy as np

# Multiplicação de escalar por matriz
matriz = np.array([ [2, -3],
                    [4, -6],
                    [6,  9]])

# print(2 * matriz)


# multiplicação entre matrizes
matriz_a = np.array([[2, 1],
                     [3, 4],
                     [5, 6]])

matriz_b = np.array([[ 7,  8,  0],
                     [10,  5, -2]])

multi_01 = matriz_a @ matriz_b
# print(multi_01)

multi_02 = np.dot(matriz_a, matriz_b)
print(multi_02)



