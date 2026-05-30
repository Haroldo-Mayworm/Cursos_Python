import numpy as np
import scipy as sp
import pandas as pd

# inicio_estudo = Tempo total de estudo (em meses)
# tempo_estudo_dia = Tempo de estudo por dia (em minutos)

nota = pd.read_excel("Aula 02 - concurso - Dados.xlsx")

## Verificando dados
# print(nota.head(len(nota)))
# print(nota.shape)
# print(nota.dtypes)
# print(nota.isnull().sum())


## Tabela da Matriz do Coeficiente
matriz_coeficiente = nota.drop(columns=["nota"])

matriz_coeficiente = matriz_coeficiente.values
# matriz_coeficiente = np.array(matriz_coeficiente)


## Tabela do Vetor das Constantes
vetor_constantes = nota.drop(columns=["inicio_estudo", "tempo_estudo_dia"])

vetor_constantes = vetor_constantes.values
# vetor_constantes = np.array(vetor_constantes)


## Estimativa dos Mínimos Quadrados
matriz_coeficiente_transposta = matriz_coeficiente.T

matriz_normal = matriz_coeficiente_transposta @ matriz_coeficiente

matriz_normal_b = matriz_coeficiente_transposta @ vetor_constantes

beta = np.linalg.inv(matriz_normal) @ matriz_normal_b

# nota = beta[0] * inicio_estudo + beta[1] * tempo_estudo_dia

resultado = nota

resultado["previsao"] = resultado["inicio_estudo"] * beta[0] + resultado["tempo_estudo_dia"] * beta[1]

## Erro médio absoluto (MAE)
from sklearn.metrics import mean_absolute_error

mean_absolute_error(resultado.nota, resultado.previsao)

resultado["erro_absoluto"] = abs(resultado.nota - resultado.previsao)

print(resultado)
