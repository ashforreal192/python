while True:
    # Infinite Loop: The while True: statement creates an infinite loop,
    # ensuring the user is repeatedly prompted until valid input is received
    number = int(input("Enter a number between 1 and 10: "))

    if 1 <= number <= 10:
        print("Thank you")
        break
    else:
        print("Number invalid, try again")