def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    if (b != 0) or (a != 0):
        return a / b
    else:
        print("Nie można dzielić przez zero!")
        return None


def zakoncz_program():
    print("Dziękujemy za skorzystanie z kalkulatora. Do widzenia!")
    quit(0)


# slownik w pythonie
operations = {
    1: dodawanie,
    2: odejmowanie,
    3: mnozenie,
    4: dzielenie,
    5: zakoncz_program
}

print("Welcome to the calculator!")
print("1) dodawanie\n"
      "2) odejmowanie\n"
      "3) mnozenie\n"
      "4) dzielenie\n"
      "5) exit\n")

while True:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    option = int(input("Wybierz operacje: "))

    operation_function = operations.get(option)
    if operation_function:
        wynik = operation_function(a, b)
        if wynik is not None:
            print("Wynik operacji: ", wynik)
    else:
        print("Wybierz opcje 1-5 !!!\n")
