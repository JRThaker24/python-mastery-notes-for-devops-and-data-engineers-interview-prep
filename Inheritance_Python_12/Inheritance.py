# Inheritance is the most important feature of object oriented programming
#Inheritance allows us to define a class which resues all the properties of another class.
#Inheritance which takes the properties of another class is called base class
#Base class: is a class from which other classes are derieved 

print("---Example of Inheritance in Python---")
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(f"Name: {self.name} Age: {self.age}")
class library(student):
    pass

vishnu = student("vishnu", 21)
vishnu.details()
        
# Private Members in Inheritance
print("\n---Example of Private Member in Inheritance in Python---")
class student:
    def __init__(self, name, age, phone):
        self.name = name
        self.__age = age
        self.__phone = phone # Here we have define Private Variable 
    def details(self):
        return f"Name: {self.name}, Age: {self.__age}, Phone: {self.__phone}"
    def phone(self):
        return self.__phone
    def age(self):
        return self.__age

class library(student):
    def __init__(self, name, age, phone, fine):
        student.__init__(self, name, age, phone)
        self.fine = fine

student1 = library("Jigar", 27, 9408009646, 800)
a = student1.details()
print(a)

print("\n Getting Private Member value outside its class")
#print(f" Studen1 Phone Number: {student1.__phone}")
#print(f" Studen1 Age: {student1.__age}")
# Direct fecth Private  details from  outside the class 
# So to return private member variable is by returning it from that classes member functions
print(f" Studen1 Phone Number: {student1.details()}")
print(f" Studen1 Phone Number: {student1.phone()}")
print(f" Studen1 Phone Number: {student1.age()}")

