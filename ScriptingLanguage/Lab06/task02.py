# Utwórz wykres słupkowy przedstawiający temperatury w poszczególnych dniach
# jakie wystąpiły w ciągu wybranego tygodnia.
# Temperatury możesz odczytywać z listy/tablicy.

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

dni = ['pon', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']
temps = [20, 21, 22, 23, 24, 15, 10]

ax.bar(dni, temps)

ax.set_ylabel('temperatura')
ax.set_title("wykres dni")

plt.show()
