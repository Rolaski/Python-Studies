# -*- coding: utf-8 -*-
def f(x):
    "Definicja funkcji"
    return 3 * x - 3


# Metoda siecznych
iter_max = 100
epsilon = 0.00001
a = 1
b = 2

for k in range(1, iter_max + 1):
    x = a - f(a) * (b - a) / (f(b) - f(a))
    if abs(f(x)) < epsilon:
        print("Rozwiązanie:", x)
        print("Liczba iteracji:", k)
        break
    a, b = b, x  # Przesunięcie granic przedziału
else:
    print("Nie udało się znaleźć rozwiązania po", iter_max, "iteracjach.")
