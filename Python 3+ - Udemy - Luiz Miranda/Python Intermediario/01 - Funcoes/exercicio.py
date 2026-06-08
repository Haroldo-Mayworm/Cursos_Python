# --- Exercício 1 - Calculadora com funções ---
# Crie uma função para cada operação abaixo.
# Cada função deve receber dois números e retornar o resultado.
# No final crie uma função "calcular(a, b, operacao)" que chama
# a função correta conforme a operação passada.
#
# Operações: soma, subtracao, multiplicacao, divisao
#
# Saída esperada:
# calcular(10, 2, "soma")           → 12
# calcular(10, 2, "subtracao")      → 8
# calcular(10, 2, "multiplicacao")  → 20
# calcular(10, 2, "divisao")        → 5.0
print("Exercício 01")

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def calcular(x, y, operacao):
    if operacao == "soma":
        return soma(x, y)
    elif operacao == "subtracao":
        return subtracao(x, y)
    elif operacao == "multiplicacao":
        return multiplicacao(x, y)
    elif operacao == "divisao":
        return divisao(x, y)
    return None

print(calcular(10, 2, "soma"))
print(calcular(10, 2, "subtracao"))
print(calcular(10, 2, "multiplicacao"))
print(calcular(10, 2, "divisao"))

# --- Exercício 2 - Analisador de lista ---
# Crie uma função "analisar(lista)" que recebe uma lista de números e retorna:
# - A quantidade de elementos
# - A soma de todos os elementos
# - A média
# - O maior valor
# - O menor valor
# - Quantos são positivos e quantos são negativos
#
# Saída esperada:
# analisar([-5, 3, 8, -2, 10, 4, -1])
#
# Quantidade : 7
# Soma       : 17
# Média      : 2.43
# Maior      : 10
# Menor      : -5
# Positivos  : 4
# Negativos  : 3
print()
print("Exercício 02")

def analisar(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = soma / quantidade
    maior = max(lista)
    menor = min(lista)
    positivos = len([n for n in lista if n > 0])
    negativos = len([n for n in lista if n < 0])

    print(f"Quantidade : {quantidade}")
    print(f"Soma       : {soma}")
    print(f"Média      : {media:.2f}")
    print(f"Maior      : {maior}")
    print(f"Menor      : {menor}")
    print(f"Positivos  : {positivos}")
    print(f"Negativos  : {negativos}")

analisar([-5, 3, 8, -2, 10, 4, -1])
