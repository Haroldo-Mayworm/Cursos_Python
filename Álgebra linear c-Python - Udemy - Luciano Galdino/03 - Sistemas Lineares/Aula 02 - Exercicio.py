import numpy as np

# ============================================
# Exercício 1 — Estimativa de Mínimos Quadrados
# ============================================
#
# Uma empresa coletou dados de horas de estudo e salário de 5 funcionários.
# O sistema abaixo é sobredeterminado (mais equações que incógnitas).
#
# | Horas de estudo | Salário (R$) |
# |      2          |    2.500     |
# |      4          |    3.200     |
# |      6          |    4.100     |
# |      8          |    4.800     |
# |      10         |    5.900     |
#
# O modelo é: salario = β₀ + β₁ * horas
#
# Tarefas:
# 1. Monte a matriz de coeficientes A (com coluna de 1s para o β₀)
# 2. Monte o vetor de constantes b (salários)
# 3. Calcule β usando a fórmula: β = (AᵀA)⁻¹ · Aᵀ · b
# 4. Exiba β₀ (intercepto) e β₁ (inclinação)
# 5. Exiba: "A cada hora de estudo o salário aumenta R$ X"

matriz_coeficientes = np.array([[1, 2],
                                [1, 4],
                                [1, 6],
                                [1, 8],
                                [1, 10], ])

matriz_coeficientes_transposta = matriz_coeficientes.T

vetor_constantes = np.array([2500, 3200, 4100, 4800, 5900])

beta = (np.linalg.inv(matriz_coeficientes_transposta @ matriz_coeficientes) @ matriz_coeficientes_transposta) @ vetor_constantes

# print(f"Salário base: R$ {beta[0]:.2f}")
# print(f"A cada hora de estudo o salário aumenta R$ {beta[1]:.2f}")

# horas_novas = 7
# salario_previsto = beta[0] + beta[1] * horas_novas
# print(f"Com {horas_novas}h de estudo o salário previsto é R$ {salario_previsto:.2f}")

# ============================================
# Exercício 2 — Regressão Linear Múltipla
# ============================================
#
# Uma imobiliária quer prever o preço de imóveis com base em:
# - Área (m²)
# - Número de quartos
# - Distância do centro (km)
#
# Dados coletados:
#
# | Área | Quartos | Distância | Preço (R$ mil) |
# |  60  |    2    |     5     |      320       |
# |  80  |    3    |     3     |      450       |
# |  100 |    3    |     8     |      400       |
# |  120 |    4    |     2     |      600       |
# |  90  |    2    |    10     |      350       |
# |  110 |    4    |     4     |      550       |
#
# O modelo é: preco = β₀ + β₁*area + β₂*quartos + β₃*distancia
#
# Tarefas:
# 1. Monte a matriz de coeficientes A (com coluna de 1s para β₀)
# 2. Monte o vetor de preços b
# 3. Calcule β usando Mínimos Quadrados
# 4. Exiba cada coeficiente com seu significado
# 5. Use o modelo para prever o preço de um imóvel com:
#    area=95, quartos=3, distancia=6

matriz_coef = np.array([[1, 60, 2, 5],
                        [1, 80, 3, 3],
                        [1, 100, 3, 8],
                        [1, 120, 4, 2],
                        [1, 90, 2, 10],
                        [1, 110, 4, 4]])

matriz_coe_transposta = matriz_coef.T

vetor_cons = np.array([320, 450, 400, 600, 350, 550])

beta_b = (np.linalg.inv(matriz_coe_transposta @ matriz_coef) @ matriz_coe_transposta) @ vetor_cons

print(f"Preço base:               R$ {beta_b[0]:.2f} mil")
print(f"A cada m² a mais:         R$ {beta_b[1]:.2f} mil")
print(f"A cada quarto a mais:     R$ {beta_b[2]:.2f} mil")
print(f"A cada km do centro:      R$ {beta_b[3]:.2f} mil")

area = 95
quartos = 3
distancia = 6

preco_previsto = beta_b[0] + beta_b[1] * area + beta_b[2] * quartos + beta_b[3] * distancia
print(f"\nImóvel: {area}m², {quartos} quartos, {distancia}km do centro")
print(f"Preço previsto: R$ {preco_previsto:.2f} mil")
