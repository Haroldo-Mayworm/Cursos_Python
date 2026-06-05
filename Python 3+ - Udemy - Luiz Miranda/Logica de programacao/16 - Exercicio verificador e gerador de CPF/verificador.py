cpf_digitado = "766.643.140-61"
cpf_limpo = "".join(filter(str.isdigit, cpf_digitado))

if len(cpf_limpo) != 11:
    print("CPF inválido")
else:
    soma_1 = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
    digito_1 = 0 if soma_1 % 11 < 2 else 11 - (soma_1 % 11)

    soma_2 = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
    digito_2 = 0 if soma_2 % 11 < 2 else 11 - (soma_2 % 11)

    if digito_1 == int(cpf_limpo[9]) and digito_2 == int(cpf_limpo[10]):
        print("CPF válido!")
    else:
        print("CPF inválido")
