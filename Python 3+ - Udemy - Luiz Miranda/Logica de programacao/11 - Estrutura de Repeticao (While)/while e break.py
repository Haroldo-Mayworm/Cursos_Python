"""
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

# condicao = True
# while condicao:
#     nome = input("Qual o seu nome: ")
#     print(f"Seu nome é {nome}")
#
#     if nome == "sair":
#         break
#
# print("Acabou")


# i = 1
# while i <= 5:
#     print(f"{i}° loop do while")
#     i += 1


qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f"{linha=} {coluna=}")
        coluna += 1
    linha += 1

print("Acabou")
