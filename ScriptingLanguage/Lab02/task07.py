import math

def rowanie_kwadratowe(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return None

def zapisz_do_pliku(nazwa_pliku, rozwiazania):
    with open(nazwa_pliku, 'w') as plik:
        if rozwiazania is not None:
            for i, rozwiazanie in enumerate(rozwiazania, start=1):
                plik.write(f"Rozwiazanie {i}: {rozwiazanie}\n")
        else:
            plik.write("Brak rozwiazan dla rownania kwadratowego o podanych wspolczynnikach.")

# Przykladowe uzycie
a = float(input("Podaj wspolczynnik a: "))
b = float(input("Podaj wspolczynnik b: "))
c = float(input("Podaj wspolczynnik c: "))

rozwiazania = rowanie_kwadratowe(a, b, c)
zapisz_do_pliku("result.txt", rozwiazania)
