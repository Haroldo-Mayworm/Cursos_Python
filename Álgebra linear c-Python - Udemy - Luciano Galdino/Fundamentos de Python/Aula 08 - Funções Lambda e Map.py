# calcular_area_retangulo = lambda base, altura: base * altura
#
# resultado = calcular_area_retangulo(2, 4)
# print(resultado)


alunos = ["Bernardo", "Caio", "Felipe", "Marcelo"]
nomes_em_maiusculo = list(map(lambda nome: nome.upper(), alunos))

print(nomes_em_maiusculo)


notas = (5, 6, 8, 9)

ponto_extra = list(map(lambda nota: nota + 1, notas))
print(ponto_extra)
