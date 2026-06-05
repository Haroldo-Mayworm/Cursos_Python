lista_itens = []

while True:
    operacao = input("O que deseja fazer (listar, inserir ou apagar)? ").lower()

    match operacao:
        case "listar" | "l":
            if len(lista_itens) == 0:
                print("Lista vazia.")
            else:
                print(*lista_itens, sep=", ")

        case "inserir" | "i":
            novo_item = input("Quais itens deseja incluir? (Separe por ',') ").lower()
            for item in novo_item.split(", "):
                lista_itens.append(item)
            print(f"Lista atualizada: {', '.join(lista_itens)}")

        case "apagar" | "a":
            print(f"Lista atual: {', '.join(lista_itens)}")
            apagar_item = input("Qual item deseja apagar? ").lower()
            if apagar_item in lista_itens:
                lista_itens.remove(apagar_item)
                print(f"Lista atualizada: {', '.join(lista_itens)}")
            else:
                print("Item não encontrado na lista.")

        case "z":
            print(f"Total de itens: {len(lista_itens)}")

        case _:
            print("Digite uma opção válida.")
