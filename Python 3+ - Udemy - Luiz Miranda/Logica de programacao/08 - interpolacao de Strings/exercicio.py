print("Exercício 01")
# --- Exercício 1 - Apresentação ---
# Usando f-string, exiba a mensagem:
# "Olá! Meu nome é [nome], tenho [idade] anos e sou de [cidade]."

nome = "Haroldo"
idade = 24
cidade = "Rio de Janeiro"

print(f"Olá! Meu nome é {nome}, tenho {idade} anos e sou de {cidade}.")


# --- Exercício 2 - Formatação de números ---
# Formate e exiba as variáveis abaixo conforme indicado:
# preco    → 2 casas decimais     ex: "Preço: R$ 19.90"
# pi       → 4 casas decimais     ex: "Pi: 3.1416"
# percent  → 1 casa decimal       ex: "Desconto: 12.5%"
print()
print("Exercício 02")

preco = 19.9
pi = 3.14159265
percent = 12.5

print(f"Preço: R$ {preco:.2f}")
print(f"Pi: {pi:.4f}")
print(f"Desconto: {percent:.1f}%")


# --- Exercício 3 - Nota fiscal simples ---
# Exiba uma nota fiscal formatada com as variáveis abaixo.
# Exemplo de saída:
# -------------------------
# Produto : Notebook
# Qtd     : 2
# Preço   : R$ 3.500,00
# Total   : R$ 7.000,00
# -------------------------
print()
print("Exercício 03")

produto = "Notebook"
quantidade = 2
preco_unitario = 3500.0

print(f"Produto : {produto}")
print(f"QTD     : {quantidade}")
print(f"Preço   : {preco_unitario:,.2f}")
print(f"Total   : {quantidade * preco_unitario:,.2f}")

# --- Exercício 4 - Tabuada ---
# Usando f-string dentro de um for, exiba a tabuada do número abaixo.
# Exemplo de saída:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
print()
print("Exercício 04")

numero = 5

for i in range(0, 13):
    print(f"{numero} x {i} = {numero * i}")


# --- Exercício 5 - Relatório de aluno ---
# Com as variáveis abaixo, exiba um relatório formatado.
# Calcule a média e exiba "Aprovado" se média >= 6, senão "Reprovado".
# Exemplo de saída:
# Aluno   : Ana
# Nota 01 : 8.0
# Nota 02 : 6.5
# Nota 03 : 7.0
# Média   : 7.17
# Status  : Aprovado
print()
print("Exercício 05")

aluno = "Ana"
nota_01 = 8.0
nota_02 = 6.5
nota_03 = 7.0

media = (nota_01 + nota_02 + nota_03) / 3
status = "Aprovado" if media >= 6 else "Reprovado"

print(f"Aluno   : {aluno}")
print(f"Nota 01 : {nota_01}")
print(f"Nota 02 : {nota_02}")
print(f"Nota 03 : {nota_03}")
print(f"Média   : {media:.2f}")
print(f"Status  : {status}")
