#4. Encapsulation in python is a concept that restricts access to certain attributes and methods of an object, 
# preventing them from being modified or accessed directly from outside the class.
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class car:
    total_cars = 0  # Class variable to keep track of the total number of cars
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        car.total_cars += 1  # Increment the total number of cars when a new car is created
    def get_car_details(self):
        return f"{self.__brand} , {self.__model}"
    
first_car = car("Mahindra", "XUV-3XO")
print(first_car.get_car_details())
#print(first_car.__brand)  # This will raise an AttributeError because __brand is private

#Now the setter method in python is used to set the value of private attribute and getter method is used to get the value of private attribute.
#Setter method
#Example of setter method in python
second_car = car("Tata", "Nexon")
print(second_car.get_car_details())
print("Total number of cars created: ", car.total_cars)  # Accessing the class variable to get the total number of cars







