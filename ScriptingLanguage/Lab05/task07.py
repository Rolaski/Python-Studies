# -*- coding: utf-8 -*-

class Pizza:
    def __init__(self, toppings):
        self._toppings = toppings
        self._pineapple_allowed = False  # domyślnie ananas nie jest dozwolony

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        self._pineapple_allowed = value


pizza = Pizza(["cheese", "tomato"])

# Ustawienie wartości pineapple_allowed na True za pomocą metody
pizza.pineapple_allowed = True

# Sprawdzenie wartości właściwości pineapple_allowed
print(pizza.pineapple_allowed)  # Output: True
