items = ["apple", "banana", "orange", "apple", "mango"]
# items = ["apple", "banana", "orange"]
# Commented array above contains terms that aren't repeated at all just for checking. Uncommend or comment accordingly.


for element in items:
    number = items.count(element)
    if number > 1:
        print("The repeated element is:", element)
        break
    else:
        continue
else:
    print("There are no repeated terms in the given array.")