x = 1

def escopo():
    global x
    x = 100

    def outra_funcao():
        x = 11
        y = 2
        print(f"Print dentro da outra função: {x=} {y=}")

    outra_funcao()
    print(f"Print dentro da função escopo: {x=}")

print(f"Print antes da função: {x=}")
escopo()
print(f"Print depois da função: {x=}")
