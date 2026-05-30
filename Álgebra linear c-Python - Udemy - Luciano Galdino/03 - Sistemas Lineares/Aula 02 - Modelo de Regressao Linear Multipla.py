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


## Tabela da Matriz
matriz_coeficiente = nota.drop(columns=["nota"])
matriz_coeficiente = matriz_coeficiente.assign(unidade=1)

matriz_coeficiente = matriz_coeficiente[["unidade", "inicio_estudo", "tempo_estudo_dia"""]]
matriz_coeficiente = matriz_coeficiente.values
matriz_coeficiente_transposta = matriz_coeficiente.T

## Tabela do Vetor das Constantes
vetor_constantes = nota.drop(columns=["inicio_estudo", "tempo_estudo_dia"])

vetor_constantes = vetor_constantes.values
# vetor_constantes = np.array(vetor_constantes)


## Regressão linear múltiplo
beta = (np.linalg.inv(
    matriz_coeficiente_transposta @ matriz_coeficiente) @ matriz_coeficiente_transposta) @ vetor_constantes

# nota = beta[0] + beta[1] * inicio_estudo + beta[2] * tempo_estudo_dia

resultado = nota
resultado["previsao"] = beta[0] + resultado["inicio_estudo"] * beta[1] + resultado["tempo_estudo_dia"] * beta[2]

## Erro médio absoluto (MAE)
from sklearn.metrics import mean_absolute_error

mean_absolute_error(resultado.nota, resultado.previsao)

resultado["erro_absoluto"] = abs(resultado.nota - resultado.previsao)

print(resultado)
