# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
# Polymorphism - The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

class Car():
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def fuel_type(self):
        return "Petrol or deisel"

class Electric_Car(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model) # inheritence by keyword super()
    def fuel_type(self):
        return "Electric Charge"


my_elec_car = Electric_Car("Tesla", "Model S")
print(my_elec_car.fuel_type())
my_car = Car("Honda", "Octavia")
print(my_car.fuel_type())