perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qnd_acertos = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes, start=1):
        print(f"Alternativa {i}: {opcao}")

    escolha = input("\nQual a opção correta: ")

    acertou = False
    qnd_opcoes = len(opcoes)

    if escolha:
        if escolha == pergunta["Resposta"]:
            acertou = True

    if acertou:
        qnd_acertos += 1
        print("Acertou!")
    else:
        print("Errou!")

print(f"\nVocê acertou {qnd_acertos} respostas de {len(perguntas)} perguntas.")
