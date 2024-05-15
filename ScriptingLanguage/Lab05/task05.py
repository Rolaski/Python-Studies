# -*- coding: utf-8 -*-

class Liczba:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if isinstance(other, Liczba):
            y = other.x
            result = self.x ** 2 + 2 * self.x * y + y
            return result
        else:
            raise TypeError("Operacja dodawania jest obsługiwana tylko dla obiektów klasy Liczba")


liczba1 = Liczba(3)  # x = 3
liczba2 = Liczba(4)  # y = 4

wynik = liczba1 + liczba2
print(wynik)
