def multiply(a, b):
    # Case 1: Both inputs are integers
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    # Case 2: One input is a string and the other is an integer
    elif isinstance(a, str) and isinstance(b, int):
        return a * b
    elif isinstance(a, int) and isinstance(b, str):
        return b * a
    # Case 3: Both inputs are strings that can be converted to integers
    try:
        a_int = int(a)
        b_int = int(b)
        return a_int * b_int
    except ValueError:
        raise ValueError("Invalid input: both inputs must be integers or one string and one integer.")



# Or simpler code:


# def multiply(p1, p2):
#     return p1 * p2


# print(multiply(8, 5))
# print(multiply('a', 5))
# print(multiply(5, 'a'))