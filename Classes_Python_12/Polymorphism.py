#Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. 
# It enables a single interface to represent different underlying forms (data types). 
# In Python, polymorphism can be achieved through method overriding and operator overloading.

class car:
    def start(self):
        print("Car is starting")

class bike:
    def start(self):
        print("Bike is starting")

class truck:
    def start(self):
        print("Truck is starting")

# Example of polymorphism using method overriding
def start_vehicle(vehicle):
    vehicle.start()
# Example of polymorphism using method overloading
def add(a, b, c=0):
    return a + b + c
