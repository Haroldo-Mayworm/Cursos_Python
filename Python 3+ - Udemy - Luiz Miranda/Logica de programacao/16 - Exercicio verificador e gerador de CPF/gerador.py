import random

cpf = [random.randint(0, 9) for _ in range(9)]

soma = sum(cpf[i] * (10 - i) for i in range(9))
digito1 = 0 if soma % 11 < 2 else 11 - soma % 11
cpf.append(digito1)

soma = sum(cpf[i] * (11 - i) for i in range(10))
digito2 = 0 if soma % 11 < 2 else 11 - soma % 11
cpf.append(digito2)

cpf_str = "".join(map(str, cpf))
cpf_formatado = f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

print(f"CPF gerado: {cpf_formatado}")
