# static methods



class Car:
    total_car = 0

    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
        # self.total_car +=1
    def fuel_type(self):
        return "Petrol or deisel"
    @staticmethod
    def general_defs():
        return "car are good"


my_car = Car("tets", "tets")
# print(my_car.general_defs())
print(Car.general_defs())   
