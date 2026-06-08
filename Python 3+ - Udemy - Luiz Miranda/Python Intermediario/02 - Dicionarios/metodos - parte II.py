# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Haroldo',
    'sobrenome': 'Mayworm',
}

# print(pessoa.get('nome', 'Não existe'))

# nome = pessoa.pop('nome')

# ultima_chave = pessoa.popitem()
# print(ultima_chave)

# pessoa.update({
#     'nome': 'novo valor - Update',
#     'idade': 30,
# })
# pessoa.update(nome='novo valor - Update-2', idade=30)
# tupla = (('nome', 'novo valor - Tupla'), ('idade', 30))
# pessoa.update(tupla)
lista = [['nome', 'novo valor - Lista'], ['idade', 30]]
pessoa.update(lista)
print(pessoa)
