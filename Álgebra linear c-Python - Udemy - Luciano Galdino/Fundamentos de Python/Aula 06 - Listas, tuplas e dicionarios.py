## Lista []
lista = [1, 5, 8, 9]

# lista[3] = 10
# print(lista[0])

lista.append(3)
# print(lista)

lista.sort()
# print(lista)

lista.insert(0, 15)
# print(lista)

lista.remove(8)
# print(lista)

lista.pop(0)
# print(lista)


## Tupla ()
nums = (1, 3, 5)

# nums.append(7)
# nums.remove(1)
## Imutável


## Dicionário
usuario = {
    "nome": "João",
    "sexo": "masculino",
    "estado": "Rio de Janeiro",
    "idade": 25,
}
# print(usuario)

usuario["país"] = "Brasil"
# print(usuario)

del usuario["estado"]
print(usuario)
