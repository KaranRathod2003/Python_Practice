#polymorphism

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