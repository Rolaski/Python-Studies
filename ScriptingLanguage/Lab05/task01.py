class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

# Tworzenie instancji klasy Cat
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)  # Oczekiwany output: ginger