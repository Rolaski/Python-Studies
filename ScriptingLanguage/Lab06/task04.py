# Narysuj wykres funkcji sin(x) i cos(x)
# dla x z zakresu od 0 do 2π.

import numpy as np

import matplotlib.pyplot as plt

x_values = np.linspace(0, 2 * np.pi)

sin_values = np.sin(x_values)
cos_values = np.cos(x_values)

plt.plot(sin_values, label='sin(x)')
plt.plot(cos_values, label='cos(x)')

plt.title('Wykresy funkcji sin(x) i cos(x)')

plt.grid(True)
plt.show()
