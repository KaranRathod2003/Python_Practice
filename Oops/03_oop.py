
#Encapsulation and inheritence also



class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand + "..."
    def full_name(self):
        return f"{self.__brand} {self.model}"
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



my_electric_car = Electric_Car("Tesla", "Model S", "90kWh")
# print(my_electric_car.model)


# print(my_electric_car.brand) we encapsulate the "brand" attribute means private
print("Brand is", my_electric_car.get_brand())


# print(my_electric_car.full_name())