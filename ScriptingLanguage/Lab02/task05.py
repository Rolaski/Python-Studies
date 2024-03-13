def sumuj_liste(lista_liczb):
    suma = sum(lista_liczb)
    return suma


def odczytaj_i_sumuj_z_pliku(nazwa_pliku, funkcja_sumowania):
    try:
        with open(nazwa_pliku, 'r') as plik:
            liczby = [float(line.strip()) for line in plik]
            suma = funkcja_sumowania(liczby)
            return suma
    except FileNotFoundError:
        print(f"Plik o nazwie {nazwa_pliku} nie został znaleziony.")
        return None
    except ValueError:
        print("Błąd: W pliku znajduje się coś innego niż liczby.")
        return None


# Testowanie programu
lista_liczb = [1, 2, 3, 4, 5]
suma_z_listy = sumuj_liste(lista_liczb)
print("Suma z listy:", suma_z_listy)

nazwa_pliku = "numbers.txt"
suma_z_pliku = odczytaj_i_sumuj_z_pliku(nazwa_pliku, sumuj_liste)

if suma_z_pliku is not None:
    print(f"Suma z pliku {nazwa_pliku}: {suma_z_pliku}")
