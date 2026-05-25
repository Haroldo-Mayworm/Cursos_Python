# --- Exercício 1 - Operações básicas ---
# Dadas as variáveis abaixo, calcule soma, subtração, multiplicação e divisão.
print("Exercício 01")

a = 18
b = 4

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


# --- Exercício 2 - Divisão inteira e resto ---
# Usando as mesmas variáveis, calcule:
# - A divisão inteira de a por b
# - O resto da divisão de a por b
print()
print("Exercício 02")

divisao_inteira = a // b
resto_divisao = a % b

print(divisao_inteira)
print(resto_divisao)


# --- Exercício 3 - Par ou ímpar ---
# Crie a variável "numero = 37"
# Use o operador % para descobrir se o número é par ou ímpar.
# Exiba: "O resto da divisão por 2 é: X"
print()
print("Exercício 03")

numero = 37

par = numero % 2 == 0
resto = numero % 2

print(f"O resto da divisão por 2 é: {resto}")
print(f"É par: {par}")


# --- Exercício 4 - Potência e raiz ---
# Calcule:
# - 3 elevado a 4
# - A raiz quadrada de 144
print()
print("Exercício 04")

potencia = 3 ** 4
raiz = 144 ** 0.5

print(potencia)
print(raiz)


# --- Exercício 5 - Calculadora de média ---
# Crie variáveis para 4 notas e calcule a média.
# Exiba: "A média é: X"
print()
print("Exercício 05")

nota_01 = 8.5
nota_02 = 7.0
nota_03 = 9.0
nota_04 = 6.5

media = (nota_01 + nota_02 + nota_03 + nota_04) / 4

print(f"A média é: {media}")
