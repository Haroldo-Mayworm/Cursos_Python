texto = "Python"

novo_texto = ""

for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)

print(novo_texto + "*")

##
numeros = range(0, 20, 2)

for numero in numeros:
    print(numero)
