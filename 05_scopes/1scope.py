username = "chaiAurCode"

def func():
    username = "chai" # But if I comment this out, the global username would be printed, not chai.
    print(username)

print(username)
func()


x = 99
def func2(y):
    z = x + y
    return z

print(func2(2))




def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()
# The provided Python code demonstrates the concept of closures, where an inner function retains
# access to variables from its enclosing function's scope even after the outer function has finished executing.'
# f1 returns the f2 function object without calling it.
# When f1() is invoked, it returns the f2 function object. At this point, f1 has completed its execution, but the returned f2
# function retains access to f1's local variable x. This combination of the function and its enclosed environment is
# known as a closure.
# Closures are useful for data encapsulation and maintaining state across function calls without using global variables or classes.



# Another example of closure:
def chaiCoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaiCoder(2)
print(f(3))
print(f)
