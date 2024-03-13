import math


def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        print("Nie można dzielić przez zero!")
        return None


def obwod_kola(r):
    return 2 * math.pi * r


def pole_kola(r):
    return math.pi * r ** 2


def zakoncz_program():
    print("Dziękujemy za skorzystanie z kalkulatora. Do widzenia!")
    quit(0)


operations = {
    1: dodawanie,
    2: odejmowanie,
    3: mnozenie,
    4: dzielenie,
    5: zakoncz_program,
    6: obwod_kola,
    7: pole_kola
}

print("Welcome to the calculator!")
print("1) dodawanie\n"
      "2) odejmowanie\n"
      "3) mnożenie\n"
      "4) dzielenie\n"
      "5) exit\n"
      "6) obwód koła\n"
      "7) pole koła\n")

while True:
    option = int(input("Wybierz operację: "))

    if option in [1, 2, 3, 4]:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
    elif option in [6, 7]:
        r = float(input("Podaj promień koła: "))
    elif option == 5:
        zakoncz_program()
    else:
        print("Wybierz opcję od 1 do 7!")
        continue

    # Użyj słownika do wywołania odpowiedniej funkcji
    operation_function = operations.get(option)
    if operation_function:
        if option in [1, 2, 3, 4]:
            wynik = operation_function(a, b)
        elif option in [6, 7]:
            wynik = operation_function(r)

        print("Wynik operacji:", wynik)
    else:
        print("Błąd: Wybierz opcję od 1 do 7!")
