ages = {"I": 78, "You": 20, "Him": 24}
print(ages["I"])
print(ages["Him"])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7]) #wyswietla 7 elementow
print(squares[7:]) #usuwa 7 elementow

print(",".join(["spam", "eggs", "spam"]))
print("Hello Me".replace("Me", "Jacob"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence"))
print("This is a sentence.".upper())
print("This is a sentence.".lower())
print("This is a sentence.".split(","))

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
print("{x},{y}".format(x=2, y=3))