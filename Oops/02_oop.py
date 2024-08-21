class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"Model will be: {self.model} ,of brand - {self.brand}"


my_new_bike = Bike("Royal Enfield", "Meteor 350")
print(my_new_bike.full_name())