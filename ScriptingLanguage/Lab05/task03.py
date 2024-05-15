class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_albumu):
        super().__init__(imie, nazwisko)
        self.numer_albumu = numer_albumu

    def __str__(self):
        return f"Student: {self.imie} {self.nazwisko}, Numer albumu: {self.numer_albumu}"

# Tworzenie trzech różnych obiektów klasy Student
student1 = Student("Anna", "Kowalska", "12345")
student2 = Student("Jan", "Nowak", "67890")
student3 = Student("Piotr", "Wiśniewski", "11223")

# Wyświetlanie informacji o studentach
print(student1)
print(student2)
print(student3)
