print("Welcome to the calculator!")
print("1) dodawanie\n"
      "2) odejmowanie\n"
      "3) mnozenie\n"
      "4) dzielenie\n"
      "5) exit\n")
while True:
    a = input("Enter a: ")
    b = input("Enter b: ")
    option = int(input("Wybierz operacje: "))

    c = 0;
    if option == 1:
        c = int(a) + int(b)
    elif option == 2:
        c = int(a) - int(b)
    elif option == 3:
        c = int(a) * int(b)
    elif option == 4:
        c = int(a) / int(b)
    elif option == 5:
        quit(3)
    else:
        print("Wybierz opcje 1-5 !!!\n")
    print("Wynik operacji: ", c)
