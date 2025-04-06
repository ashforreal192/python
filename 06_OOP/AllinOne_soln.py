class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand + " !"
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"    

my_car = Car("Mercedes", "AMG")
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())
print(my_car.get_brand())
print(my_car.fuel_type())


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    

my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.fullName())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())



# __init__ Method: This special method, known as the initializer or constructor,
# is automatically invoked when a new instance of the class is created.
# Its primary purpose is to initialize the object's attributes. In this case, it initializes:​

# self.brand: Assigned the value of the brand parameter.​
# self.model: Assigned the value of the model parameter.


# Now we can use this class in a generalized manner as well:
my_new_car = Car("Rolls Royce", "Phantom")
print(my_new_car.brand)
print(my_new_car.model)