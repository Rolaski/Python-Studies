# Narysuj wykres kołowy przedstawiający
# rozkład procentowy różnych gatunków owoców w koszu.
# Przyjmij, że dane na temat owoców to
# lista krotek np.
# data = [('jabłka', 30), ('gruszki', 20),
# ('śliwki', 15), ('banany', 25), ('cytryny', 10)]

import matplotlib.pyplot as plt

data = [('jabłka', 30), ('gruszki', 20), ('śliwki', 15), ('banany', 25), ('cytryny', 10)]

labels, sizes = zip(*data)

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Rozkład procentowy różnych gatunków owoców w koszu')
plt.show()
