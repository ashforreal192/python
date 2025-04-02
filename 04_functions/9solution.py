# THE CORRECT CODE:
def evn_generator(limitt):
    for x in range(2, limitt + 1, 2):
        yield x
for num in evn_generator(15):
    print(num)





# Wrong code, cuz we aren't looking for a list. But still wrote because sheer thinking is worth something.
def even_generator(limit):
    myList = []
    for i in range(2, limit + 1, 2):
        myList.append(i)
        print(myList)

even_generator(15)