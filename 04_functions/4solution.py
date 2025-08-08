import math

def circleDets(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return circumference, area

a, c = circleDets(5)
# This line calls the circleDets function and passes 5 as the radius.
# The function runs and returns two values. Python "unpacks" these two values into the variables a and c.

print("Area: ", round(a, 2), "Circumference: ", round(c, 2))
# This line prints the results, but the labels are accidentally swapped.
# It prints the value of a (which is the circumference) next to the label "Area: ".
# It prints the value of c (which is the area) next to the label "Circumference: ".
# The round(..., 2) function just rounds the numbers to two decimal places for a cleaner look.