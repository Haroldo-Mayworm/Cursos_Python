def soma(x, y):
    if x > 10: return [10, 20]
    return x + y


soma1 = soma(2, 2)
soma2 = soma(3, 3)


# print(soma1)
# print(soma2)
# print(soma1 + soma2)
#
# print(soma(11, 55))

###
def soma_n_argumentos(*args):
    return sum(args)


soma_1 = soma_n_argumentos(1, 2, 3)
# print(soma_1)

soma_2 = soma_n_argumentos(4, 5, 6)
# print(soma_2)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma_n_argumentos(*numeros)
print(outra_soma)

print(sum(numeros))
print(*numeros)
