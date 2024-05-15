# -*- coding: utf-8 -*-

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_albumu):
        super().__init__(imie, nazwisko)
        self.numer_albumu = numer_albumu

    def przedstaw_sie(self):
        print(f"Cześć, nazywam się {self.imie} {self.nazwisko} i mój numer albumu to {self.numer_albumu}")

# Tworzenie trzech różnych obiektów klasy Student
student1 = Student("Anna", "Kowalska", "12345")
student2 = Student("Jan", "Nowak", "67890")
student3 = Student("Piotr", "Wiśniewski", "11223")

# Studenci się przedstawiają
student1.przedstaw_sie()
student2.przedstaw_sie()
student3.przedstaw_sie()
