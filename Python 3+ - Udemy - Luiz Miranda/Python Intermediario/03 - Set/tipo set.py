# Sets - Conjuntos em Python (tipo set)

## Criando
set_1 = set()  # vazio
set_2 = {'Luiz', 1, 2, 3}  # com dados
set_3 = set("Haroldo")

# print(set_1, type(set_1))
# print(set_2, type(set_2))
# print(set_3, type(set_3))

## Peculiaridades
# Sets são eficientes para remover valores duplicados de iteráveis.
lista_repetida = [1, 2, 3, 3, 3, 2, 1, 4, 1, 2, 3]
set_lista = set(lista_repetida)
lista_unica = list(set_lista)
# print(lista_unica)

# print(4 in set_lista)
# print(2 not in set_lista)
# for numero in set_lista:
# print(numero)

## Métodos
# add, update, clear, discard
set_inicial = set()
set_inicial.add("Haroldo")
set_inicial.add(25)
# set_inicial.update("iteravel")
set_inicial.update(("iteravel no ite", 10, 20))

# set_inicial.clear()
set_inicial.discard("iteravel no ite")

# print(set_inicial)

## Operadores
# união "|"
# intersecção "&"
# diferença "-"
# diferença simétrica "^"
s1 = {1, 2, 3}
s2 = {2, 3, 4}

set_uniao = s1 | s2
set_interseccao = s1 & s2
set_diferenca = s1 - s2
set_dif_simetrica = s1 ^ s2

print(set_uniao)
print(set_interseccao)
print(set_diferenca)
print(set_dif_simetrica)
