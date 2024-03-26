# -*- coding: utf-8 -*-
import math


def wartosc(x):
    return 3 * x - math.cos(x) - 1  # równanie 3x - cos(x) - 1 = 0


epsilon = 0.00001  # margines błędu
a = 0.25  # lewy koniec przedziału
b = 0.75  # prawy koniec przedziału
iteracje = 0
x2 = 0

x1 = a - (wartosc(a) / (wartosc(b) - wartosc(a))) * (b - a)

if wartosc(x1) * wartosc(a) < 0:
    while True:
        x2 = x1 - (wartosc(x1) / (wartosc(a) - wartosc(x1)) * (a - x1))
        iteracje += 1

        if abs(wartosc(x2)) <= epsilon:
            break
        else:
            x1 = x2

elif wartosc(x1) * wartosc(b) < 0:
    while True:
        x2 = x1 - (wartosc(x1) / (wartosc(b) - wartosc(x1)) * (b - x1))
        iteracje += 1

        if abs(wartosc(x2)) <= epsilon:
            break
        else:
            x1 = x2

print("liczba iteracji:", iteracje)
print("wynik x2:", x2)
print("wartość funkcji f(x2):", wartosc(x2))
