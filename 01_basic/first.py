print("Chai and python")

def chai(n): # a function called chai is defined here with a value of "n"
    print(n)
chai(4) # 4 would simply be printed
chai("lemon tea") # lemon tea (a string) would be printed.
#Now the function called chai would be exported from this file to the file called second.py, so check that out.

chai_one = "ginger tea"
chai_two = "masala chai"
chai_three = "kada tea"
# important: I entered the above two variables after I imported python in my terminal. But the python shell
# doesn't get reloaded automatically so even after pressing ctrl+s,
# it didn't get saved/reloaded. So for the purpose of new entries being reloaded,
# we use a command called "from importlib import reload". And then write "reload(filename)". In
# this case, reload(first). After that we can access the new variables using command....  first.chai_one




# If you run this in the shell:

# python
# >>> import first
# >>> first.chai_one
# 'ginger tea'

# If you later modify first.py (e.g., change chai_one to "mint tea"), you must reload:

# python
# >>> from importlib import reload
# >>> reload(first)
# >>> first.chai_one
# 'mint tea'