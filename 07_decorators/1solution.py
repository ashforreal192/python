import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} sec time")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)

example_function(2)


# Execution Flow:

# Python encounters @timer and immediately calls timer(example_function)

# timer() returns the wrapper function, replacing example_function

# When calling example_function(2), you're actually calling wrapper(2)




# Inside wrapper:

# start = time.time() captures the pre-execution timestamp

# func(*args, **kwargs) invokes the original example_function with argument 2

# During execution, time.sleep(2) blocks for 2 seconds

# end = time.time() captures the post-execution timestamp

# The duration is calculated and printed

# The result (None in this case) is returned




# Closure Behavior:

# The wrapper maintains a reference to the original func through closure

# All arguments (*args, **kwargs) are forwarded to the wrapped function

# The decorator preserves the original function's signature and return value