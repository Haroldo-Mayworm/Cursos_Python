frase = "       Olha só que   , coisa interessante          "
lista_frases_cruas = frase.split(",")

lista_frases = [frase.strip() for frase in lista_frases_cruas]

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ", ".join(lista_frases)
# print(frases_unidas)
