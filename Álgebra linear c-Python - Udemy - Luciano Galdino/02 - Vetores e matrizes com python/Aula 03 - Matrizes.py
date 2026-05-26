import numpy as np

lista_matriz = [[1, -2, 3],
                [-4, 5, 6],
                [7, 8, -9]]

matriz = np.array(lista_matriz)


matriz_um = np.ones((2,3))
# print(matriz_um)

matriz_zero = np.zeros((2,3))
# print(matriz_zero)

matriz_diagonal = np.diag((2,4,6,8))
# print(matriz_diagonal)

matriz_identidade01 = np.identity(4)
# print(matriz_identidade01)

matriz_identidade02 = np.eye(2)
# print(matriz_identidade02)

matriz_transporta = matriz.T
# print(matriz.T)

matriz_oposta = -1*matriz
# print(matriz_oposta)


matriz_linha = np.array([[1,2,3,4,5]])
print(matriz_linha.shape)

matriz_coluna = np.array([[1],[2],[3],[4],[5]])
print(matriz_coluna.shape)









