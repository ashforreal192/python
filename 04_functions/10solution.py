def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return "Number invalid"
    else:
        return num * factorial(num - 1)
    
print(factorial(10))
print(factorial(0))
print(factorial(-10))