import numpy as np
import pandas as pd

massa = pd.read_csv("Aula 08 - inspecao.csv", sep=";")

# Valores Nulos
massa.isnull().sum()
massa = massa.dropna()

# Matriz de Covariância
matriz = massa.drop(columns=["amostra"])

matriz = matriz.values

matriz_cov = np.cov(np.transpose(matriz))

# Autovalor e autovetor
autovalor, autovetor = np.linalg.eig(matriz_cov)

print(f"O autovalor {autovalor[0]:.3f} está associado aos autovetores {autovetor[0][0]:.3f} e {autovetor[1][0]:.3f}.")
print(f"O autovalor {autovalor[1]:.3f} está associado aos autovetores {autovetor[0][1]:.3f} e {autovetor[1][1]:.3f}.")

# Taxa de variância explicada
evr = autovalor / np.sum(autovalor)

# print(evr)
