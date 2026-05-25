"""
Fatiamento de strings

 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
"""

variavel = "Olá mundo"

print(len(variavel))
print(variavel[1:8:])
print(variavel[0:len(variavel):2])
print(variavel[-1:-10:-1])
