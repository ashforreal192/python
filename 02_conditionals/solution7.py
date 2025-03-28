order_size = "Medium"
extra_shot = False

if extra_shot:
    coffee = order_size + " With extra shot"
else:
    coffee = order_size + " Normal coffee"


print("Your order is:", coffee)