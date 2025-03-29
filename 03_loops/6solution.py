number = 10
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    
    
    # the code under is basically the same thing as the above just written better:
    
    factorial *= number
    number -= 1
    
    print(factorial)