# Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model  # Use a protected attribute for the model

    @property
    def model(self):
        return self.__model  # Return the model attribute
    
class Electric_car(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
    
new_car = Car("Honda", "Civic")
new_car2 = Electric_car("Tesla", "s", "100KWH")

print(isinstance(new_car, Car))
print(isinstance(new_car2, Electric_car))
print(new_car.brand)
print(new_car2.brand)
print(new_car.model) # Accessing the model attribute using the property decorator

new_car.model = "Accord" # This will raise an AttributeError because the model attribute is read-only