# Narysuj wykres punktowy
# przedstawiający zależność
# masy ciała od wzrostu dla grupy osób.

import matplotlib.pyplot as plt
import numpy as np
import random

plt.style.use('_mpl-gallery')

np.random.seed(3)
wzrost = np.random.normal(170, 10, 100)  # średnia 170 cm, odchylenie standardowe 10 cm, 100 wartości
waga = np.random.normal(70, 15, 100)  # średnia 70 kg, odchylenie standardowe 15 kg, 100 wartości

fig, ax = plt.subplots()

ax.scatter(wzrost, waga, alpha=0.7, edgecolors='w', s=50, c='b')

ax.set_xlabel('Wzrost (cm)')
ax.set_ylabel('Waga (kg)')
ax.set_title('Zależność masy ciała od wzrostu')

plt.show()

# DRUGA WERSJA

# losujemy wartosci dla naszych ludzi
wzrost = [random.randint(100, 200) for _ in range(10)]
masa_ciala = [random.randint(50, 120) for _ in range(10)]

plt.scatter(wzrost, masa_ciala, color='blue', marker='o')

plt.title('Zależność masy ciała od wzrostu')
plt.xlabel('Wzrost (cm)')
plt.ylabel('Masa ciała (kg)')

plt.show()
