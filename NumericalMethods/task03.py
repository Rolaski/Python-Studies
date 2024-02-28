def bisekcja(f, a, b, epsilon):
    """
    Metoda bisekcji do znajdowania pierwiastka równania f(x) = 0.

    Argumenty:
      f: funkcja f(x)
      a: lewy koniec przedziału
      b: prawy koniec przedziału
      epsilon: dokładność

    Zwraca:
      Przybliżenie pierwiastka
    """

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


# Przykład użycia
def f(x):
    return pow(x,3) + x - 1


a = 0
b = 1
epsilon = 0.01

pierwiastek = bisekcja(f, a, b, epsilon)

print(f"Przybliżenie pierwiastka: {pierwiastek}")
