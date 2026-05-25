print("Exercício 01")
# --- Exercício 1 - Apresentação pessoal ---
# Crie variáveis para armazenar seu nome, idade e cidade.
# Exiba a mensagem: "Meu nome é -, tenho - anos e moro em -."

nome = "Haroldo"
idade = 24
local = "Rio de Janeiro"

print(f"Meu nome é {nome}, tenho {idade} anos e moro em {local}.")

# --- Exercício 2 - Troca de variáveis ---
# Troque os valores de a e b SEM usar uma terceira variável.
print()
print("Exercício 02")

a = 10
b = 20

a, b = b, a

print(a)  # esperado: 20
print(b)  # esperado: 10


# --- Exercício 3 - Calculadora simples ---
# Crie duas variáveis numéricas e calcule soma, subtração, multiplicação e divisão.
# Exiba cada resultado em uma linha.
print()
print("Exercício 03")

numero_01 = 15
numero_02 = 5

soma = numero_01 + numero_02
subtracao = numero_01 - numero_02
multiplicacao = numero_01 * numero_02
divisao = numero_01 / numero_02

print(f"Números - {numero_01} e {numero_02}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

# --- Exercício 4 - Tipos de dados ---
# Crie uma variável de cada tipo e use type() para confirmar.
# Tipos: int, float, str, bool
print()
print("Exercício 04")

v_inteira = 1
v_float = 2.5
v_str = "Variável do tipo string"
v_bool = True

print(type(v_inteira))
print(type(v_float))
print(type(v_str))
print(type(v_bool))

# --- Exercício 5 - Correção de nomes ---
# Corrija os nomes das variáveis abaixo seguindo as convenções do Python (PEP 8):
print()
print("Exercício 05")

# 1nome = "Ana"
# Idade-Pessoa = 25
# SALARIO mensal = 3500.0
# valor_Total = 100

nome = "Ana"
idade_pessoa = 25
salario_mensal = 3500.0
valor_total = 100
