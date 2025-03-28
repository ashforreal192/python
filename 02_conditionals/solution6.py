Distance = 5

if Distance < 3:
    transport = "Walk"
elif Distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of: ",transport)