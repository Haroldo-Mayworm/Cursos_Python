# pessoa = dict(nome="Haroldo", sobrenome="Mayworm"...)
pessoa = {
    "nome": "Haroldo",
    "sobrenome": "Mayworm",
    "idade": 25,
    "altura": 1.81,
    "endereços": [
        {
            "rua": "tal tal",
            "número": 123,
        },
        {
            "rua": "outra rua",
            "número": 321,
        },
    ],
}
print(type(pessoa))
print(pessoa["nome"])
print(pessoa["sobrenome"])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
