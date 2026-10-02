# Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor."
    
new_car = Car("Toyota", "Camry")
print(new_car.general_description()) # why it prints the general description of a car even though it is called on an instance of the class?

# explain why it prints the general description because the static method is not bound to any instance of the class. It can be called on the class itself or on an instance of the class, but it does not have access to the instance's attributes or methods.
#  In this case, calling new_car.general_description() simply calls the static method and returns the general description of a car, regardless of the specific instance (new_car) it was called on.