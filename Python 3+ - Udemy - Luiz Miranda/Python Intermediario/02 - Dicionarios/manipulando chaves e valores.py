# Manipulando chaves e valores em dicionários
pessoa = {}

chave = "nome"

pessoa[chave] = "Haroldo"
pessoa["sobrenome"] = "Mayworm"

print(pessoa[chave])

pessoa[chave] = "Maria"

del pessoa["sobrenome"]
print(pessoa)
print(pessoa["nome"])

# print(pessoa.get("sobrenome"))
if pessoa.get("sobrenome") is None:
    print("NÃO EXISTE")
else:
    print(pessoa["sobrenome"])
