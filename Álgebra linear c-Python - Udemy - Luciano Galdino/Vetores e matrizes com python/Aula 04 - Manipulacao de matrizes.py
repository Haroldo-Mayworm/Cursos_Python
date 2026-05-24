import numpy as np

matriz = np.array([ [1, -2, 3],
                    [-4, 5, 6],
                    [7, 8, -9]])

matriz_copia = matriz.copy()
# print(matriz_copia)

matriz_copia[0,1] = 9
# print(matriz_copia)


matriz_linha = matriz_copia[2,:]
print(matriz_linha)

matriz_coluna = matriz_copia[:,1]
print(matriz_coluna)
