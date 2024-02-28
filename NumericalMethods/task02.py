def horner_dzielenie(wspolczynniki_w, wspolczynniki_d):
    """
    Dzieli wielomian o współczynnikach 'wspolczynniki_w' przez dwumian o współczynnikach 'wspolczynniki_d'
    schematem Hornera.

    Argumenty:
      wspolczynniki_w: lista współczynników wielomianu W(x)
      wspolczynniki_d: lista współczynników dwumianu D(x)

    Zwraca:
      tuple: (iloraz, reszta)
    """

    # Sprawdzenie długości list
    if len(wspolczynniki_w) < len(wspolczynniki_d):
        raise ValueError(
            "Długość listy współczynników wielomianu musi być większa lub równa długości listy współczynników dwumianu.")

    # Inicjowanie zmiennych
    iloraz = [0] * (len(wspolczynniki_w) - len(wspolczynniki_d) + 1)
    reszta = wspolczynniki_w[-len(wspolczynniki_d):]

    # Dzielenie schematem Hornera
    for i in range(len(wspolczynniki_d)):
        iloraz[-i - 1] = reszta[0]
        for j in range(1, len(reszta)):
            reszta[j - 1] = reszta[j] - iloraz[-i - 1] * wspolczynniki_d[j]
        reszta[-1] = reszta[-1] - iloraz[-i - 1] * wspolczynniki_d[-1]

    return iloraz, reszta


# Przykład użycia
wspolczynniki_w = [3, 2, -5, 4]
wspolczynniki_d = [1, -2]

iloraz, reszta = horner_dzielenie(wspolczynniki_w, wspolczynniki_d)

print(f"W(x) = (x - 1) * ({iloraz[0]}x^2 + {iloraz[1]}x + {iloraz[2]}) + {reszta[0]}")
