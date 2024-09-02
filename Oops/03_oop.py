# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
# Encapsulation - Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.



# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
# Inheritence - One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class. 



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

my_car =  Car("Toyota", "Supra")
print(my_car.get_brand()) # we encapsulate the "brand" attribute means private
# print("Brand is", my_electric_car.brand)


# print(my_electric_car.full_name())