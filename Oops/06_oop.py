# Static methods

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @staticmethod
    def method_static():
        return f"it is static method"


my_car = Car("Toyota", "Supra")
print(Car.method_static())  # Correct usage
