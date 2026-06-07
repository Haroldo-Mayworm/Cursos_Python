import numpy as np

matriz = np.array([[3, 0],
                   [0, 1]])

autovalor, autovetor = np.linalg.eig(matriz)

print(autovalor)
print(autovetor)
