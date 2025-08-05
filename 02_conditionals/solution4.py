fruit = "Banana"
color = "Green"


# Initialize the State variable to handle cases where the fruit is not "Banana"
State = "Fruit invalid"

if fruit == "Banana":
    if color == "Yellow":
        State = "Ripe"
    elif color == "Green":
        State = "Unripe"
    elif color == "Brown":
        State = "Overripe"
    else:
        State


print("Fruit:",fruit,"\nColor:",color,"\nState:",State)