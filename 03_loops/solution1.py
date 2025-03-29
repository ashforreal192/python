numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_num_count = 0

for num in numbers:
    if num > 0:
        print(num)
        positive_num_count += 1

print("Final count of all the positive numbers is:", positive_num_count)