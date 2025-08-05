input_str = "teeteracdacd"

# --- Task 1: Print all characters first ---
print("All characters in the string:")
for char in input_str:
  print(char)

# Add a separator for clarity
print("---") 

# --- Task 2: Find and print the first non-repeated character ---
for char in input_str:
  # Check if the character appears only once in the entire string
  if input_str.count(char) == 1:
    print("First non-repeated char is:", char)
    break # This command exits the loop immediately after finding the first match