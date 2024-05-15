# -*- coding: utf-8 -*-

class Student:
    def __init__(self, name, album_number):
        self.name = name
        self.album_number = album_number


student1 = Student("Michał Kowalska", "123345")
student2 = Student("Jan Nowak", "675890")
student3 = Student("Marcepan Wiśniewski", "112253")

print(f"Student 1: {student1.name}, Album number: {student1.album_number}")
print(f"Student 2: {student2.name}, Album number: {student2.album_number}")
print(f"Student 3: {student3.name}, Album number: {student3.album_number}")
