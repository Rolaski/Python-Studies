# -*- coding: utf-8 -*-
import math
import sys
from sympy import symbols, diff, Abs

x = symbols('x')
f = x ** 3 + x ** 2 - 3 * x - 3
f_diff = diff(f, x)
f_diff2 = diff(f_diff, x)


# Maksymalna liczba iteracji, która będzie wykonywana w poszukiwaniu rozwiązania.
iter_max = 100
epsilon = 0.00001

# Przedziały dla zadania
a = math.pi / 2.0 + 0.1
b = math.pi

if f_diff.subs(x, a) * f_diff2.subs(x, a) > 0 or f_diff.subs(x, b) * f_diff2.subs(x, b) > 0:
    print("Warunek spełniony: f(x0) * f''(x0) > 0. Metoda stycznych będzie działać poprawnie.")
else:
    print("Uwaga: Warunek niespełniony: f(x0) * f''(x0) <= 0. Metoda stycznych może nie być zbieżna.")
    sys.exit()

# Pętla iteracyjna wykonująca metodę stycznych.
for k in range(1, iter_max + 1):
    a_new = a - f.subs(x,a) / f_diff2.subs(x,a)  # corrected typo here
    if Abs(f.subs(x, a_new)).evalf() < epsilon or a_new >= b:
        print("Rozwiązanie:", a_new)
        print("Liczba iteracji:", k)
        break
    a = a_new
else:
    print("Nie udało się znaleźć rozwiązania po", iter_max, "iteracjach.")

