# --- Exercício 1 - Contagem regressiva ---
# Faça uma contagem regressiva de 10 até 0 usando while.
# Ao chegar em 0 exiba: "Lançamento!"
#
# Saída esperada:
# 10
# 9
# ...
# 1
# 0
# Lançamento!
print("Exercício 01")

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
# print("Lançamento!")


# --- Exercício 2 - Adivinhe o número ---
# Crie uma variável "numero_secreto = 7"
# Use while para ficar pedindo um palpite até o usuário acertar.
# A cada erro exiba: "Errou! Tente novamente."
# Ao acertar exiba: "Parabéns! Você acertou!"
#
# Dica: use input() para capturar o palpite do usuário
print()
print("Exercício 02")

# numero_secreto = 7
# tentativa_usuario = 0
#
# while tentativa_usuario != numero_secreto:
#     tentativa_usuario = int(input("Tente acerta o número (1-10): "))
#     if tentativa_usuario != numero_secreto:
#         print("Errou! Tente novamente")
# print("Parabéns! Você acertou")

# --- Exercício 3 - Acumulador ---
# Fique pedindo números ao usuário com input() até ele digitar 0.
# Ao final exiba a soma de todos os números digitados.
#
# Saída esperada:
# Digite um número (0 para sair): 5
# Digite um número (0 para sair): 3
# Digite um número (0 para sair): 0
# Soma total: 8
print()
print("Exercício 03")

numero_digitado = 1
soma = 0

while numero_digitado:
    numero_digitado = int(input("Digite um número (0 para sair): "))
    soma += numero_digitado
    if numero_digitado == 0:
        print(f"Soma total: {soma}")
