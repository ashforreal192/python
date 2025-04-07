# In Python, the @property decorator allows you to define methods in a class that can be accessed
# like attributes, providing a way to implement managed attributes without the need for explicit
# getter and setter methods. This approach enhances code readability and encapsulation by allowing
# you to add logic that is executed when an attribute is accessed or modified



# Example of using @property decorators:

class Thermometer:
    def __init__(self, temperature=0.0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._temperature = value


thermo = Thermometer()
thermo.temperature = 25.0
print(thermo.temperature)  # Outputs: 25.0





# As opposed to:
# Implementing Setters and Deleters:

# You can also define setter and deleter methods for a
# property using the @<propertyname>.setter and @<propertyname>.deleter decorators:


class Thermometer:
    def __init__(self, temperature=0.0):
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._temperature = value


thermo = Thermometer()
thermo.set_temperature(25.0)
print(thermo.get_temperature())  # Outputs: 25.0



# Contrasting the Two Approaches:

# Attribute-Like Access:

# Explicit Getter/Setter: Accessing or modifying the temperature requires calling methods (get_temperature() and set_temperature(value)),
# which can be less intuitive and more verbose.​

# @property Decorator: The temperature can be accessed and modified like a regular attribute (thermo.temperature),
# enhancing readability and making the interface more natural.​

# Encapsulation and Validation:

# Both Approaches: Allow for encapsulation and validation. The setter method in both cases
# ensures that temperatures below absolute zero are not set.​

# Code Maintainability:

# Explicit Getter/Setter: If the internal implementation changes, all code interacting
# with the class must use the getter and setter methods, which can be cumbersome.​

# @property Decorator: Allows internal changes without affecting the external interface,
# as interactions remain consistent with attribute access.
