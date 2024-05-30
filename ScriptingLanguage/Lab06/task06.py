# Narysuj wykres słupkowy przedstawiający
# liczbę urodzonych dzieci
# według płci w danym roku.
# Przyjmij, że dane na temat urodzeń
# to lista krotek np.
# dane = [(100, 90), (110, 95), (120, 105), (130, 110)]
# Dla podanej listy wykres może wyglądać następująco

import matplotlib.pyplot as plt
import numpy as np

rok = ['2020', '2021', '2022', '2023']
wartosci = {
    'chlopcy': (100, 110, 120, 130),
    'dziewczeta': (90, 95, 105, 110),
}

x = np.arange(len(rok))
width = 0.30
mul = 0

fig, ax = plt.subplots(layout='constrained')

for a, b in wartosci.items():
    offset = width * mul
    rec = ax.bar(x + offset, b, width, label=a)
    ax.bar_label(rec, padding=3)
    mul += 1

ax.set_ylabel("ilosc urodzonych")
ax.set_title('rok')
ax.set_xticks(x + width / 2, rok)
ax.legend(loc="upper left", ncols=2)
ax.set_ylim(0, 150)

plt.show()
