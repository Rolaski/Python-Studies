# -*- coding: utf-8 -*-
import math


# Definicja funkcji f(x)
def f(x):
    return math.sin(x) - 0.5 * x


# Definicja funkcji df(x), która oblicza wartość pochodnej funkcji sin(x) - 0.5 * x.
def df(x):
    return math.cos(x) - 0.5


# Maksymalna liczba iteracji, która będzie wykonywana w poszukiwaniu rozwiązania.
iter_max = 100
epsilon = 0.01

# Przedziały dla zadania
x = math.pi / 2 + 0.1
right_boundary = math.pi

# Pętla iteracyjna wykonująca metodę stycznych.
for k in range(1, iter_max + 1):
    x_new = x - f(x) / df(x)
    if abs(f(x_new)) < epsilon or x_new >= right_boundary:
        print("Rozwiązanie:", x_new)
        print("Liczba iteracji:", k)
        break
    x = x_new
else:
    print("Nie udało się znaleźć rozwiązania po", iter_max, "iteracjach.")
