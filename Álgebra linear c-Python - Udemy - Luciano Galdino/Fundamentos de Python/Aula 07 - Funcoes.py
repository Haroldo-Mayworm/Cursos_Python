# def calcular_area_retangulo(base, altura):
#     area = base * altura
#     return area
#
# resultado = calcular_area_retangulo(4, 3)
# print(resultado)


# def numero_maior(num1, num2):
#     if num1 > num2:
#         print(f"{num1} é maior que {num2}")
#     elif num2 > num1:
#         print(f"{num2} é maior que {num1}")
#     else:
#         print(f"{num1} é igual a {num2}")
#
# numero_maior(1, 3)


def calculo_pitagoras(cateto1, cateto2, hipotenusa):
    if cateto1 == "":
        calculo_cateto = (hipotenusa**2 - cateto2**2)**(1/2)
        print(f"O cateto é {calculo_cateto}")
    elif cateto2 == "":
        calculo_cateto = (hipotenusa**2 - cateto1**2)**(1/2)
        print(f"O cateto é {calculo_cateto}")
    else:
        calculo_hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
        print(f"A hipotenusa é {calculo_hipotenusa}")
calculo_pitagoras(3, 4, "5")
