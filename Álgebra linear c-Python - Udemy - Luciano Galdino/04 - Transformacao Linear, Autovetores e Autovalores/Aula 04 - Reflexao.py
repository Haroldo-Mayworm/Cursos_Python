import numpy as np
import matplotlib.pyplot as plt

# Vetor que receberá a transformação
vetor_re = np.array([4, 1])

# Matriz
matriz = np.array([[1, 0],
                   [0, -1]])

# Matriz para transformação
matriz_t = matriz @ vetor_re

# Coordenadas do vetor
x = [0, vetor_re[0]]
y = [0, vetor_re[1]]

x_t = [0, matriz_t[0]]
y_t = [0, matriz_t[1]]

plt.plot(x, y, color="blue")
plt.plot(x_t, y_t, color="red")
plt.show()
