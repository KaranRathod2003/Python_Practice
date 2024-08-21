class Bike: #class
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

my_bike = Bike("Royal Enfield", "Meteor 350") #object
print(my_bike.brand)
print(my_bike.model)