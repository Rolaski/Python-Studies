# Narysuj wykres funkcji
# y = x^2 dla x z zakresu od -5 do 5.

import matplotlib.pyplot as plt

x = [i for i in range(-5, 5 + 1)]
y = [i ** 2 for i in x]

plt.plot(x, y)
plt.grid(True)
plt.show()
