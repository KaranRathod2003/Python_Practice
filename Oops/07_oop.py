# Problem: Add a static method to the Car class that returns a general description of a car.

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    
    @staticmethod
    def method_static():
        return f"it is static method"
    
    @property
    def model(self):
        return self.__model


my_car = Car("Toyota", "Supra")
print(Car.method_static())  
# my_car.model = "corolla"
# print(my_car.model()) object is not callable
print(my_car.model) 