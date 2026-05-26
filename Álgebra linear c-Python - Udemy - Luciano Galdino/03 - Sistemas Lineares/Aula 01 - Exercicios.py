import numpy as np
import scipy as sp

# --- Exercício 1 - Sistema 3x3 ---
# Resolva o sistema abaixo usando a Regra de Cramer.
# Implemente uma função e chame com a matriz e vetor corretos.
#
#  2x +  y -  z =  8
# -3x - y + 2z = -11
# -2x + y + 2z =  -3
print("Exercício 01")


def cramer3(_matriz, _vetor):
    determinante = sp.linalg.det(np.array([_matriz[:, 0], _matriz[:, 1], _matriz[:, 2]]).T)
    if not np.isclose(determinante, 0):
        determinante_x = sp.linalg.det(np.array([_vetor[:], _matriz[:, 1], _matriz[:, 2]]).T)
        determinante_y = sp.linalg.det(np.array([_matriz[:, 0], _vetor[:], _matriz[:, 2]]).T)
        determinante_z = sp.linalg.det(np.array([_matriz[:, 0], _matriz[:, 1], _vetor[:]]).T)

        x = determinante_x / determinante
        y = determinante_y / determinante
        z = determinante_z / determinante

        print(f"O valor de X é: {x}")
        print(f"O valor de Y é: {y}")
        print(f"O valor de Z é: {z}")
    else:
        print("O determinante da matriz dos coeficientes é nula")


matriz_01 = np.array([[2, 1, -1],
                      [-3, -1, 2],
                      [-2, 1, 2]])

vetor_01 = np.array([8, -11, -3])

cramer3(matriz_01, vetor_01)

# --- Exercício 2 - Validação ---
# O sistema abaixo tem determinante zero — o código deve identificar isso.
# Reuse a função cramer3() e verifique se ela trata corretamente.
#
#  1x + 2y + 3z =  5
#  2x + 4y + 6z = 10
#  3x + 6y + 9z = 15
#
# Dica: observe as linhas da matriz — o que você nota?
print()
print("Exercício 02")

matriz_02 = np.array([[1, 2, 3],
                      [2, 4, 6],
                      [3, 6, 9]])

vetor_02 = np.array([5, 10, 15])

cramer3(matriz_02, vetor_02)
