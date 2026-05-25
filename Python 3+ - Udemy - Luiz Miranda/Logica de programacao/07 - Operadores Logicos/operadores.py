# Operadores lógicos
# and (e), or (ou), not (não), in (está em) e not in (não está em)

# and - Todas as condições precisam ser verdadeiras.
# or - Qualquer condição verdadeira avalia
# not - Usado para inverter expressões
# in - Está em algum lugar
# not in - não está em algum lugar

#Também existe o tipo None usado para representar nulo

## AND e OR
entrada = input("[E]ntrar ou [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123"

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")


## NOT
print(not True)
print(not False)


## IN e NOT IN
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
