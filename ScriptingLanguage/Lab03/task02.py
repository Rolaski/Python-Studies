size = int(input("Enter size of array: "))
array = []

# Wyplenij tablice znakami pobieranymi od uzytkownika
for i in range(size):
    char = input("Enter Char: ")
    array.append(char)

# Wyswietl znaki w odwrotnej kolejnosci
print("Revers array:", ", ".join(array[::-1]))

