def horner():
    liczba = int(input("Podaj liczbę współczynników: "))
    print("")

    tab = [0] * liczba
    tab2 = [0] * liczba
    tab3 = [0] * liczba
    tab2[-1] = 0

    for i in range(liczba - 1, -1, -1):
        if i > 0:
            tab[i] = float(input(f"Podaj liczbę przy współczynniku x^{i}: "))
        else:
            tab[i] = float(input("Podaj wyraz wolny: "))

    argument = float(input("Podaj argument: "))

    for i in range(liczba - 1, -1, -1):
        tab3[i] = tab[i] + tab2[i]
        if i > 0:
            tab2[i - 1] = argument * tab3[i]

    print("")

    for i in range(liczba - 1, -1, -1):
        print(f"\t{tab[i]}", end="")

    print("\n")
    print(argument, end="")

    for i in range(liczba - 1, -1, -1):
        print(f"\t{tab2[i]}", end="")

    print("\n")
    for i in range(liczba - 1, -1, -1):
        print(f"\t{tab3[i]}", end="")

    print("\n")

    print("Wielomian Q(x): ", end="")
    for i in range(liczba - 1, 0, -1):
        print(f"{tab3[i]}x^{i - 1}", end="")
        if i > 1:
            print(" + ", end="")

    if tab3[0] > 0:
        print(f" + {tab3[0]}/x-{argument}")

    print("\n")

    print(f"Wartość podanej funkcji w punkcie x = {liczba} to: {tab3[0]}")
    print("")


if __name__ == "__main__":
    horner()
