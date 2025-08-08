# THE CORRECT CODE:
def evn_generator(limitt):
    for x in range(2, limitt + 1, 2):
        yield x
for num in evn_generator(15):
    print(num)
# Why limitt + 1?:
# Let's say limitt is 10. If you wrote range(2, 10, 2), the sequence would be 2, 4, 6, 8. It would stop before 10. To make sure the number 10 is included in the sequence, you must provide a stop value that is greater than 10. By using limitt + 1 (which is 11), you ensure the range includes 10.


# Another example
def odd_gen(limitttt):
    for a in range(3, limitttt + 1, 3):
        yield a

for number in odd_gen(48):
    print(number)




# Wrong code, cuz we aren't looking for a list. But still wrote because sheer thinking is worth something.
def even_generator(limit):
    myList = []
    for i in range(2, limit + 1, 2):
        myList.append(i)
        print(myList)

even_generator(15)