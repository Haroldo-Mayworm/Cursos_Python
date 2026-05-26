import numpy as np
import scipy as sp
from scipy import linalg

# x + 2y + 3z = 2
# 2x - y + z = -1
# -2x - 3y + 3z = -11

# Matriz dos coeficientes
matriz = np.array([[1, 2, 3],
                   [2, -1, 1],
                   [-2, -3, 3]])

# Vetor das constantes
vetor = np.array([2, -1, -11])


# Função Cramer 3x3 - 3 Linha e 3 Incógnitas
def cramer3(_matriz, _vetor):
    determinante = sp.linalg.det(np.array([_matriz[:, 0], _matriz[:, 1], _matriz[:, 2]]).T)
    if not np.isclose(determinante, 0):

        determinante_x = sp.linalg.det(np.array([_vetor[:], _matriz[:, 1], _matriz[:, 2]]).T)
        determinante_y = sp.linalg.det(np.array([_matriz[:, 0], _vetor[:], _matriz[:, 2]]).T)
        determinante_z = sp.linalg.det(np.array([_matriz[:, 0], _matriz[:, 1], _vetor[:]]).T)

        x = determinante_x / determinante
        y = determinante_y / determinante
        z = determinante_z / determinante

        print(f"O valor de x é {x:.2f}")
        print(f"O valor de y é {y:.2f}")
        print(f"O valor de z é {z:.2f}")
    else:
        print("O determinante da matriz dos coeficientes é nula")


cramer3(matriz, vetor)
