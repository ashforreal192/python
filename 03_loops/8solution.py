while True:
    
    number = int(input("Enter a prime number: "))

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("Number is not prime, try again")
                break
        else:
            print("Number is prime, good")
            break
    else:
        print("Number must be greater than one, so please try again.")



# A simpler code:
# Will only run after the first one is completed executing after a prime number is entered

entered_number = 28

is_prime = True

if entered_number > 1:
    for i in range(2, entered_number):
        if (entered_number % i) == 0:
            is_prime = False
            break

print(is_prime)