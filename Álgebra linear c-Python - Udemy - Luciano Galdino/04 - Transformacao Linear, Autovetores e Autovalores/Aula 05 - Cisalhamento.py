import numpy as np
import matplotlib.pyplot as plt

# Vetor que receberá a transformação
vetor_c = np.array([2, 2])

# Constante
k = 3

# Matriz
matriz = np.array([[1, k],
                   [0, 1]])

# Matriz para transformação
matriz_t = matriz @ vetor_c

# Coordenadas do vetor
x = [vetor_c[0], vetor_c[0]]
y = [0, vetor_c[1]]

x_t = [matriz_t[1] + 2, matriz_t[0]]
y_t = [0, matriz_t[1]]

plt.plot(x, y, color="blue")
plt.plot(x_t, y_t, color="red")
plt.show()
