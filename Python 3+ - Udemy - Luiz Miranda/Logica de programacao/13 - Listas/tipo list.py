lista_a = ["Luiz", 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = "Maria"

# print(lista_a)
# print(lista_b)

##
lista = [10, 20, 30, 40]

del lista[2]
lista.pop()
lista.append(60)
lista.append(70)
# lista.clear()
print(lista)

lista.insert(0, 500)
print(lista)
