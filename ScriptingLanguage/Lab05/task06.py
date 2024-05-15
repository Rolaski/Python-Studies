# -*- coding: utf-8 -*-

class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def print_dog_info():
        print("Number of dogs:", Dog.count)
        print("Dog names:", ', '.join(Dog.dogs))

# Tworzenie dwóch obiektów klasy Dog
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Wywoływanie metody bark na obiektach
dog1.bark(2)
dog2.bark(1)

# Wywoływanie metody statycznej do wypisania informacji o psach
Dog.print_dog_info()
