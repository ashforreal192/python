string = "Lallu bhosdika"
reversed_string = ""
non_reversed_string = "" # just for reference


for char in string:
    reversed_string = char + reversed_string
    non_reversed_string = non_reversed_string + char
    print(char + 1)

print(reversed_string)
print(non_reversed_string)