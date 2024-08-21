# class variable - Track how many cars are made



class Car:
    total_car = 0

    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
        # self.total_car +=1
    def fuel_type(self):
        return "Petrol or deisel"

class Electric_Car(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model) # inheritence by keyword super()
    def fuel_type(self):
        return "Electric Charge"


Electric_Car("test", "test")
Car("test", "test")
print(Car.total_car)