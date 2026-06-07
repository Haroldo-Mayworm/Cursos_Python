import numpy as np
import matplotlib.pyplot as plt

# Vetor que receberá a transformação
vetor_a = np.array([4, 2])

# Constante
# Alongamento: k > 1
# Contração: 0 < k < 1
k = 2
# k = 0.5

# Matriz
matriz = np.array([[k, 0],
                   [0, 1]])

# Matriz para transformação
matriz_t = matriz @ vetor_a

# Coordenadas do vetor
x = [0, vetor_a[0]]
y = [vetor_a[1], vetor_a[1]]

x_t = [0 + 6, matriz_t[0] + 6]
y_t = [matriz_t[1], matriz_t[1]]

plt.plot(x, y, color="blue")
plt.plot(x_t, y_t, color="red")
plt.show()
