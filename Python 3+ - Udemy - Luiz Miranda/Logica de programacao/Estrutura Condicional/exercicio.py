# --- Exercício 1 - Maior de idade ---
# Crie uma variável "idade" e verifique se a pessoa é maior ou menor de idade.
# Exiba: "Maior de idade" ou "Menor de idade"
print("Exercício 01")

idade = 18

if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


# --- Exercício 2 - Número positivo, negativo ou zero ---
# Crie uma variável "numero" e verifique se é positivo, negativo ou zero.
# Exiba o resultado.
print()
print("Exercício 02")

numero = -10

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Número zero")


# --- Exercício 3 - Nota e conceito ---
# Crie uma variável "nota" (0 a 10) e exiba o conceito:
# nota >= 9            → "A"
# nota >= 7            → "B"
# nota >= 5            → "C"
# nota < 5             → "Reprovado"
print()
print("Exercício 03")

nota = 6

if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
else:
    print("Reprovado")


# --- Exercício 4 - Login simples ---
# Crie variáveis "usuario" e "senha".
# Se usuario == "admin" e senha == "1234" exiba "Acesso liberado"
# Caso contrário exiba "Acesso negado"
print()
print("Exercício 04")

usuario = "admin"
senha = "1234"

if usuario == "admin" and senha == 1234:
    print("Acesso liberado")
else:
    print("Acesso negado")
