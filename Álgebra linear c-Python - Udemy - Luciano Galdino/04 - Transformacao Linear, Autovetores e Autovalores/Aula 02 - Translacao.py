import numpy as np
import matplotlib.pyplot as plt

# Vetor que receberá a transformação
vetor_t = np.array([[3, 2],
                    [2, 5]])

# Matriz
matriz = np.array([[4, 1],
                   [4, 1]])

# Transformação
matriz_t = vetor_t + matriz

# Coordenadas do vetor
x = [vetor_t[0][0], vetor_t[1][0]]
y = [vetor_t[0][1], vetor_t[1][1]]

x_t = [matriz_t[0][0], matriz_t[1][0]]
y_t = [matriz_t[0][1], matriz_t[1][1]]

plt.plot(x, y, color="blue")
plt.plot(x_t, y_t, color="red")
plt.show()
