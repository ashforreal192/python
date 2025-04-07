class Car:
    # __init__ Method: This special method, known as the initializer or constructor,
    # is automatically invoked when a new instance of the class is created.
    # Its primary purpose is to initialize the object's attributes. In this case, it initializes:​

    # self.brand: Assigned the value of the brand parameter.​
    # self.model: Assigned the value of the model parameter.
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.brand + " !"
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are a means of transport"
    # @staticmethod decorator is used to define a static method within a class.
    # Static methods are methods that belong to the class itself rather than any particular instance of the class.
    # They do not require access to instance-specific data (self) or class-specific data (cls).
    # This makes them suitable for utility functions that are
    # logically related to the class but do not need to interact with instance or class attributes


    # Key Characteristics of Static Methods:

    # No Access to Instance or Class Data: Static methods do not have access to instance (self) or class (cls) variables.
    # They operate independently of class or instance-specific data. ​

    # Called on the Class or Instance: Static methods can be called on the class itself or on instances of the class. ​
    # Vultr Docs

    # Defined Using @staticmethod: The @staticmethod decorator is used to define a static method.

    # In summary, the @staticmethod decorator in Python is a way to define methods that are logically related to a class
    # but do not require access to instance or class-specific data.
    # This allows for cleaner and more organized code, especially when defining utility functions within classes.

my_car = Car("Mercedes", "AMG")
print(Car.total_cars)
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())
print(my_car.get_brand())
print(my_car.fuel_type())


print(Car.general_description())


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    

my_tesla = ElectricCar("Tesla", "Model S", "85 kWh")
print(Car.total_cars)
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.fullName())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

print(isinstance(my_tesla, Car)) #Boolean response to show if my_tesla is an instance of Car and ElectricCar.
print(isinstance(my_tesla, ElectricCar))


safari = Car("Tata", "Safari") # An instance of Car class
print(Car.total_cars)
print(safari.brand)
print(safari.model)
print(safari.fullName())
print(safari.fuel_type())


safari2 = ElectricCar("BMW", "X3", "60kWh") # An instance of Electric car class
print(Car.total_cars)
print(safari2.brand)
print(safari2.model)
print(safari2.fullName())
print(safari2.fuel_type())



# Application of multiple-inheritance
class Battery:
    def __init__(self):
        self.battery_capacity = "100 kWh"
        self.battery_health = "Good"

    def battery_info(self):
        return f"Capacity: {self.battery_capacity}, Health: {self.battery_health}"
    
    def charge_battery(self):
        return "Battery is charging..."
    
    def battery_status(self):
        return "Battery is at 80%."


class Engine:
    def __init__(self):
        self.horsepower = "670 HP"
        self.engine_type = "Electric"

    def engine_info(self):
        return f"Engine Type: {self.engine_type}, Horsepower: {self.horsepower}"
    
    def engine_status(self):
        return "Engine running smoothly."


class ElectricCarTwo(Car, Battery, Engine):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)
        Battery.__init__(self)
        Engine.__init__(self)


# Example usage:
e_car = ElectricCarTwo("Tesla", "Model S")
print(e_car.fullName())           # From Car
print(e_car.battery_info())       # From Battery
print(e_car.battery_status())     # From Battery
print(e_car.charge_battery())     # From Battery
print(e_car.engine_info())        # From Engine
print(e_car.engine_status())      # From Engine






# Now we can use this class in a generalized manner as well:
my_new_car = Car("Rolls Royce", "Phantom")
print(Car.total_cars)
print(my_new_car.brand)
print(my_new_car.model)