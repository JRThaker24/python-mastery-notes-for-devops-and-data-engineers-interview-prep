# Python is object oriented Programming language: 
#Objects are used to represent real life (<_>) and in order to create an object we must declare template or blue print of the object called class.
# Syntax class:
# class name:
#    variable = value
#    def func():

print(" --- Examples of class in Python--- ")
class person:
    def func(self, name, age, Gender):
        self.name = name
        self.age = age
        self.Gender = Gender
    def getdetails(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Gender: {self.Gender}")

student1 = person()
#print(p1)
student1.func("Jigar", 27, "Male")
student1.getdetails()
person.getdetails(student1)

print(" --- Examples of class in Python using Constructor--- ")
class person2:
    def __init__(self, name, age, Gender):
        self.name = name
        self.age = age
        self.Gender = Gender
        print(f"Name: {self.name}\n Age: {self.age}\n Gender: {self.Gender}")
    def getdetails(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Gender: {self.Gender}")

student2 = person2("Vishnu", 21, "Male")
#student2.getdetails()
#person2.getdetails(student2)

student3 = person2("Rahul", 22, "Male")
student3.getdetails()

#Class variables & Instance Variables
# Variables at class levels called class variable and Variables at Instance level called instance Variables
#So instance variables are unique to each instance and Class variables are common to all and shared between the objects and class.

print("---Example of class variable---")
class numbers:
    n = []
    def __init__(self, val):
        self.n.append(val)

even = numbers(2)
print(even.n)
odd =  numbers(3)
print(odd.n)


print("\n---Example of Instance variable---")
class numbers:
    def __init__(self, val):
        self.n = []
        self.n.append(val)


    def adddeatils(self, val):
        self.n.append(val)
odd = numbers(3)
even = numbers(2)

print(odd.n)
print(even.n)
odd.adddeatils(7)
even.adddeatils(4)
print(odd.n)
print(even.n)