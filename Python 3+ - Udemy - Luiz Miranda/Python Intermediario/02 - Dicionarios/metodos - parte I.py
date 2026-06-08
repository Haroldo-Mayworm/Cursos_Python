# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    "nome": "Haroldo",
    "sobrenome": "Mayworm",
    "idade": 25,
}

pessoa.setdefault("idade", 0)
# print(pessoa["idade"])
print(len(pessoa))

print(pessoa)
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))
