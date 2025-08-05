string = "Lallu bhosdika"
reversed_string = ""
non_reversed_string = "" # just for reference


for char in string:
    reversed_string = char + reversed_string
    non_reversed_string = non_reversed_string + char
    print(char)

print("Reversed string:\n", reversed_string)
print("Non reversed string:\n", non_reversed_string)