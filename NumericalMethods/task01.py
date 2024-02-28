def horner(wspolczynniki, x):

  wynik = 0 # Inicjujemy zmienną 'wynik' wartością 0
  for i in range(len(wspolczynniki)):
    wynik = wynik * x + wspolczynniki[i]
  return wynik

# Przykład użycia
wspolczynniki = [3, 2, -5, 4]
x = 2

wartosc_w_punkcie = horner(wspolczynniki, x)

print(f"Wartość wielomianu o współczynnikach {wspolczynniki} w punkcie {x} wynosi: {wartosc_w_punkcie}")
