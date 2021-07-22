# Inputs and Outputs
"""
name = input("Hello whats your name? ")
print("Good morning " + name)
age = input("and how old are you? ")
print("thats cool")
"""
# Arrays
"""
list = ["Volvo", "Chevrolet", "Audi"]
print(list[2])
"""
# Array Functions
"""
list = ["Volvo", "Chevrolet", "Audi"]
list.insert(1, "Corona")
list.remove("Corona") 
list.clear()
list.pop()
list.index("Volvo)
"""
# Functions
"""
def myFirstFunction():
    print("Hello this is my first function! ")
print("NEW PROGRAM")
myFirstFunction()
"""
# Return Function
"""
def powerNumber(number):
    return number * number
print("NEW PROGRAM")
print(powerNumber(3))
"""
# If & Else
"""
age = 0
if age >= 18:
    print("Overage")
elif age < 18 and age > 0:
    print("Underage")
else:
    print("Not even born")
"""
# While Loops
"""
i = 0
while i < 4:
    print("Haha")
    i += 1
print("End of the loop")
"""
# For Loopss
"""
fruits = ["apple", "orange", "banana"]
for x in fruits:
    print(x)
"""
# Class & Objects
"""
class Student:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career
student = Student("Andre", 22, "systems engineering")
print(student.name)
print(student.age)
print(student.career)
"""
# Class Methods
"""
class Student:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career
    def calculateSalaryByAge(self):
        if self.age < 60 and self.age >= 18:
            return 3000
        else:
            return 0
student = Student("Andre", 22, "Systems Engineering")
print(student.calculateSalaryByAge())
"""
