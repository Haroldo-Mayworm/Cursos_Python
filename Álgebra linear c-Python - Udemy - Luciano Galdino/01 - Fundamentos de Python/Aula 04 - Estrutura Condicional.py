nota = float(input("Digite sua nota: "))
media = 7

if nota >= media:
    print("Aprovado")
elif media > nota >= 6:
    print("Recuperação")
else:
    print("Reprovado")
