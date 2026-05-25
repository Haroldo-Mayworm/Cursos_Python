nome = "Haroldo"
idade = 24
altura = 1.81

texto = "Nome={var1} idade={var2} altura={var3}".format(var1=nome, var2=idade, var3=altura)

texto_02 = "Nome={var1} idade={var2} altura={var3}"
formato = texto_02.format(var1=nome, var2=idade, var3=altura)

print(texto)
print(formato)
