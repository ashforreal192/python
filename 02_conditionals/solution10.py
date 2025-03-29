animal = "Dog"
age = 1

if animal == "Dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"
elif animal == "Cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Adult cat food"
else:
    food = "Animal's age or species aren't according to the protocol"

print(food)
