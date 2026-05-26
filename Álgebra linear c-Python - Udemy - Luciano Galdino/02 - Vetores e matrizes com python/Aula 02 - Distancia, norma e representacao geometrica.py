import numpy as np
import matplotlib.pyplot as plt

## Distância

vetor_01 = np.array([2, -4, 1])
vetor_02 = np.array([3, 2, -5])

def distancia_entre_vetores(vetor1, vetor2):
    soma_quadrado = 0
    for i in range(len(vetor1)):
        soma_quadrado += (vetor1[i] - vetor2[i]) ** 2
    distancia = np.sqrt(soma_quadrado)
    print(f"A distância entre os vetores é igual a: {distancia:.2f}")

# distancia_entre_vetores(vetor_01, vetor_02)


## Norma
def norma_vetores(vetor):
    soma_quadrado = 0
    for i in range(len(vetor)):
        soma_quadrado += (vetor[i] ** 2)
    norma = np.sqrt(soma_quadrado)
    print(f"{norma:.2f}")

# norma_vetores(vetor_01)
# norma_vetores(vetor_02)

normaVetor01 = np.linalg.norm(vetor_01)
normaVetor02 = np.linalg.norm(vetor_02)

# print(f"{normaVetor01:.2f}")
# print(f"{normaVetor02:.2f}")


## Representação Geométrica
vetor_m = np.array([4, 5])
vetor_p = np.array([-2, 5])
soma = []

for i in range(len(vetor_m)):
    soma.append(vetor_m[i] + vetor_p[i])

vetor_v = np.array([vetor_m, vetor_p, soma])
origem = np.array([[0, 0, 0], [0, 0, 0]])

plt.quiver(*origem, vetor_v[:,0], vetor_v[:,1], color=["r", "b", "y"], scale=35)
plt.show()




