import random

size = int(input("Enter the size of the array: "))

array = [random.uniform(-5, 5) for _ in range(size)]

with open("result.txt", "w") as file:
    for num in array:
        file.write(str(num) + "\n")

print("Array values have been written to result.txt file.")
