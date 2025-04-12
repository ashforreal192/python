def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        result = func(*args, **kwargs)
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return result
    return wrapper

@debug
def hello():
    print("hello")
hello()

@debug
def greet(name, greeting = "hello"):
    print(f"{greeting}, from {name}")
greet("chai", greeting = "hanji")