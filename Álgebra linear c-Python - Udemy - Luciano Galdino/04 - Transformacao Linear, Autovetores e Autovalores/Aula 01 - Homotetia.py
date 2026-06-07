import numpy as np
import matplotlib.pyplot as plt

# Vetor que receberá a transformação
vetor_h = np.array([2, 1])

# Parâmetro de proporção
k = 3

# Matriz
matriz = np.array([[k, 0],
                   [0, k]])

# Matriz transformação
matriz_t = matriz @ vetor_h

print(matriz_t)

# Coordenadas do vetor
x = [vetor_h[0], 0]
y = [0, vetor_h[1]]

x_t = [matriz_t[0], 0]
y_t = [0, matriz_t[1]]

plt.plot(x, y, color="blue")
plt.plot(x_t, y_t, color="red")

plt.show()
