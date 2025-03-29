given_number = 4

for i in range(1, 11):
    if i == 5:
        continue
    print(given_number, "*", i, "=", given_number*i)
else:
    print("Multiplication table completed successfully.")


    # Else Clause: In Python, a loop's else clause executes after the
    # loop completes
    # all iterations without encountering a break statement