"""
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_usuario = input("Vou dobrar o número que vc digitar: ")

# if numero_usuario.isdigit():
#     numero_float = float(numero_usuario)
#     print(f"O dobro de {numero_usuario} é {numero_float * 2:.2f}")
# else:
#     print("Isso não é um número")

try:
    numero_float = float(numero_usuario)
    print(f"O dobro de {numero_usuario} é {numero_float * 2:.2f}")
except:
    print("Isso não é um número")
