class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"

my_car = Car("Mercedes", "AMG")
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())


# __init__ Method: This special method, known as the initializer or constructor,
# is automatically invoked when a new instance of the class is created.
# Its primary purpose is to initialize the object's attributes. In this case, it initializes:​

# self.brand: Assigned the value of the brand parameter.​
# self.model: Assigned the value of the model parameter.


# Now we can use this class in a generalized manner as well:
my_new_car = Car("Rolls Royce", "Phantom")
print(my_new_car.model)