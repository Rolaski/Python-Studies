# -*- coding: utf-8 -*-
import sys
from sympy import symbols, diff, Abs

x = symbols('x')
f = x ** 3 + x ** 2 - 3 * x - 3
f_diff = diff(f, x)
f_diff2 = diff(f_diff, x)

# Metoda siecznych
iter_max = 100
epsilon = 0.00001
a = 1.0
b = 2.0

if f_diff.subs(x, a) * f_diff2.subs(x, a) > 0 or f_diff.subs(x, b) * f_diff2.subs(x, b) > 0:
    print("Warunek spełniony: f(x0) * f''(x0) > 0. Metoda stycznych będzie działać poprawnie.")
else:
    print("Uwaga: Warunek niespełniony: f(x0) * f''(x0) <= 0. Metoda stycznych może nie być zbieżna.")
    sys.exit()

for k in range(1, iter_max + 1):
    x_new = a - f.subs(x, a) * (b - a) / (f.subs(x, b) - f.subs(x, a))
    if Abs(f.subs(x, x_new)) < epsilon:
        print("Rozwiązanie:", x_new)
        print("Liczba iteracji:", k)
        break
    a, b = b, x_new  # Przesunięcie granic przedziału
else:
    print("Nie udało się znaleźć rozwiązania po", iter_max, "iteracjach.")
