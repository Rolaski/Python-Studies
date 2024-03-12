def bisekcja(f, a, b, epsilon):
    # Argumenty:
    #   f: funkcja f(x)
    #   a: lewy koniec przedziału
    #   b: prawy koniec przedziału
    #   epsilon: dokładność

    licznik_iteracji = 0

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c, licznik_iteracji
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        licznik_iteracji += 1

    return (a + b) / 2, licznik_iteracji


# Przykład użycia
def f(x):
    return pow(x, 3) + x - 1


a = 0
b = 1
epsilon = 0.01
pierwiastek, iteracje = bisekcja(f, a, b, epsilon)

print(f"Przybliżenie pierwiastka: {pierwiastek}")
print(f"Liczba iteracji: {iteracje}")
