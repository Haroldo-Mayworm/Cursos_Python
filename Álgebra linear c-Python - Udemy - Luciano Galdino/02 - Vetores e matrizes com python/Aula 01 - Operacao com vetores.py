import numpy as np
from xarray.backends import refresh_engines

lista_numero = [2, -4, 1]
array_lista = np.array(lista_numero)

# print(type(lista_numero))
# print(type(array_lista))
# print(array_lista.shape)
# print(len(array_lista))

vetor_01 = np.array([2, -4, 1])
vetor_02 = np.array([3, 2, -5])

# Soma
def soma_vetores(vetor01, vetor02):
    return vetor01 + vetor02

# print(soma_vetores(vetor_01, vetor_02))

# Multiplicação
produto_interno = 0

for i in range(len(vetor_01)):
    produto_interno += vetor_01[i] * vetor_02[i]

# print(produto_interno)


# Multiplicação por Escalar
numero_escalar = 5

multiplicacao_escalar = numero_escalar * vetor_01

print(multiplicacao_escalar)
