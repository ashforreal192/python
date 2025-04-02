import math

def circleDets(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return circumference, area

a, c = circleDets(5)
print("Area: ", round(a, 2), "Circumference: ", round(c, 2))