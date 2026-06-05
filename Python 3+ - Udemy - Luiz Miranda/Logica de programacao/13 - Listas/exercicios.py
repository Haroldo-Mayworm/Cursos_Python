# --- Exercício 1 - Gerenciador de notas ---
# Você tem a lista de notas abaixo.
# Realize as seguintes tarefas:
#
# 1. Adicione a nota 9.5 no final da lista
# 2. Remova a menor nota da lista
# 3. Ordene a lista em ordem crescente
# 4. Exiba a maior nota, a menor nota e a média
# 5. Exiba quantas notas estão acima de 7.0
#
# Saída esperada:
# Maior nota : 9.5
# Menor nota : 5.0
# Média      : 7.5
# Acima de 7 : X notas
print("Exercício 01")

notas = [7.0, 5.5, 8.0, 6.5, 9.0, 5.0, 8.5]

notas.append(9.5)
notas.remove(min(notas))
notas.sort()

maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

acima_de_7 = len([nota for nota in notas if nota > 7.0])

print(f"Maior nota : {maior}")
print(f"Menor nota : {menor}")
print(f"Média      : {media:.1f}")
print(f"Acima de 7 : {acima_de_7} notas")

# --- Exercício 2 - Carrinho de compras ---
# Você tem um carrinho de compras como lista de tuplas (produto, preco).
# Realize as seguintes tarefas:
#
# 1. Adicione o produto ("Fone de Ouvido", 199.90) ao carrinho
# 2. Exiba todos os produtos e seus preços formatados
# 3. Calcule e exiba o total do carrinho
# 4. Exiba o produto mais caro
# 5. Exiba os produtos em ordem de preço (mais barato ao mais caro)
#
# Saída esperada:
# Notebook        R$ 3.500,00
# Mouse           R$   150,00
# ...
# Total: R$ X.XXX,XX
# Mais caro: Notebook
print()
print("Exercício 02")

carrinho = [
    ("Notebook", 3500.00),
    ("Mouse", 150.00),
    ("Teclado", 250.00),
    ("Monitor", 1200.00),
]

carrinho.append(("Fone de Ouvido", 199.90))

for produto, preco in carrinho:
    print(f"{produto:<15} R$ {preco:>8.2f}")

total = sum(preco for _preco, preco in carrinho)
print(f"\nTotal: R$ {total:,.2f}")

mais_caro = max(carrinho, key=lambda p: p[1])
print(f"Mais caro: {mais_caro[0]}")

print("\nOrdem por preço:")
for produto, preco in sorted(carrinho, key=lambda p: p[1]):
    print(f"  {produto:<15} R$ {preco:>8.2f}")
