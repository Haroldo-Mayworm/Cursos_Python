import numpy as np
import matplotlib.pyplot as plt

# Vetor que receberá a transformação
vetor_r = np.array([4, 1])

# pi radiano = 180 graus
# Ângulo de rotação 30° (pi/6 radianos)
alfa = (np.pi / 2)

# Matriz
matriz = np.array([[np.cos(alfa), (-np.sin(alfa))],
                   [np.sin(alfa), np.cos(alfa)]])

# Matriz para transformação
matriz_t = matriz @ vetor_r

# Coordenadas do vetor
x = [0, vetor_r[0]]
y = [0, vetor_r[1]]

x_t = [0, matriz_t[0]]
y_t = [0, matriz_t[1]]

plt.plot(x, y, color="blue")
plt.plot(x_t, y_t, color="red")
plt.show()
