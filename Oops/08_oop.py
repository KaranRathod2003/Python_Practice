# class Battery:
#     def battery_info(self):
#         return "This is Batttery"
# class ElectricCar(Battery, Car):
#     pass



# class Engine:
#     def engine_info(self):
#         return "this is engine"
# class Car:
#     def car_info(self):
#         return "this is car"



# my_electric_car = ElectricCar()
# print(my_electric_car.battery_info)
# print(my_electric_car.engine_info)
# print(my_electric_car.car_info)


class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class Car:
    def car_info(self):
        return "This is Car"

class ElectricCar(Battery, Engine, Car):  # Multiple inheritance
    pass

# Create an instance of ElectricCar
my_electric_car = ElectricCar()

# Call methods from all inherited classes
print(my_electric_car.battery_info())  # Output: This is Battery
print(my_electric_car.engine_info())   # Output: This is Engine
print(my_electric_car.car_info())      # Output: This is Car
