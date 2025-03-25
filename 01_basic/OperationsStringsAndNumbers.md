--------------------sTRING OPERATIONS-----------------------------

Case Folding
casefold() → Converts the string to lowercase, optimized for case-insensitive comparisons.
Example: "ß".casefold() → 'ss'

Center Alignment
center(width, fillchar) → Centers the string in a field of given width, optionally using fillchar.
Example: "Hello".center(10, "-") → "--Hello--"

Padding with Zeros
zfill(width) → Pads the string with zeros on the left until it reaches the specified width.
Example: "42".zfill(5) → '00042'

Expand Tabs
expandtabs(tabsize) → Converts tabs (\t) to spaces, with an optional tab size.
Example: "A\tB".expandtabs(4) → "A B"

Partitioning
partition(separator) → Splits the string into three parts: before, separator, after.
Example: "I like tea".partition("like") → ('I ', 'like', ' tea')

rpartition(separator) → Like partition() but starts from the right.

Splitting Lines
splitlines(keepends=False) → Splits a string at line breaks into a list.
Example: "Hello\nWorld".splitlines() → ['Hello', 'World']

Checking Start/End Characters
startswith(prefix[, start, end]) → Checks if the string starts with prefix.
Example: "Python".startswith("Py") → True

endswith(suffix[, start, end]) → Checks if the string ends with suffix.
Example: "Python".endswith("on") → True

String Justification
ljust(width, fillchar) → Left-aligns the string in a field of given width.
Example: "Hi".ljust(5, "-") → 'Hi---'

rjust(width, fillchar) → Right-aligns the string in a field of given width.
Example: "Hi".rjust(5, "-") → '---Hi'

Translation Using Mapping
maketrans() → Creates a mapping table for translate().
Example:
trans = str.maketrans("aeiou", "12345")
"hello".translate(trans) # → 'h2ll4'
Checking Content Type

isdecimal() → Checks if all characters are decimals.
Example: "123".isdecimal() → True

isnumeric() → Checks if all characters are numeric (including superscripts).
Example: "²³".isnumeric() → True

isprintable() → Checks if all characters are printable.
Example: "\n".isprintable() → False

Count Substrings
count(substring, start, end) → Counts occurrences of a substring within a range.
Example: "banana".count("a") → 3

Finding Substrings
find(substring, start, end) → Returns the first index of a substring or -1 if not found.
Example: "hello".find("e") → 1

rfind(substring, start, end) → Like find() but searches from the right.

Remove Prefix/Suffix
removeprefix(prefix) → Removes the specified prefix (Python 3.9+).
Example: "unwanted_word".removeprefix("un") → 'wanted_word'

removesuffix(suffix) → Removes the specified suffix (Python 3.9+).
Example: "filename.txt".removesuffix(".txt") → 'filename'

Checking Substring Membership
in → Check if a substring exists in a string.
Example: 'tea' in "I love tea" → True

String Multiplication
Repeat the string using _.
Example: "ha" _ 3 → 'hahaha'

Sorting Characters
sorted(string) → Returns a sorted list of characters.
Example: sorted("python") → ['h', 'n', 'o', 'p', 't', 'y']

Reversing a String
Slicing: [::-1] → Reverses the string.
Example: "Python"[::-1] → 'nohtyP'

Immutable Strings
Strings in Python are immutable, meaning you cannot change characters directly.
To modify, you can create a new string. Example:
s = "hello"
s = s.replace("h", "H") # → 'Hello'

Concatenation: Combine strings using +.
Example: "Hello" + " World"

Repetition: Repeat a string using _.
Example: "Hi" _ 3

Indexing: Access specific characters using indices.
Example: "Python"[0] → 'P'

Slicing: Extract substrings using slicing (start:end:step).
Example: "Python"[1:4] → 'yth'

Length: Get the length of the string using len().
Example: len("Python") → 6

Case Conversion:
lower() → Convert to lowercase.
upper() → Convert to uppercase.
capitalize() → Capitalize the first letter.
title() → Capitalize each word.
swapcase() → Swap cases.

String Search:
find() → Find the first occurrence of a substring.
rfind() → Find the last occurrence.
inde() → Like find(), but raises an error if not found.
count() → Count occurrences of a substring.

Replace/Substitute:
replace() → Replace substrings.
translate() → Replace characters via translation table.

Trimming:
strip() → Remove whitespace from both ends.
lstrip() → Remove leading whitespace.
rstrip() → Remove trailing whitespace.
Split and Join:
split() → Split a string into a list.
join() → Combine a list into a string.

Membership Testing: Check if a substring exists using in.
Example: 'Py' in "Python" → True

String Formatting:
format() → Basic formatting.

f-strings → Modern string interpolation.
Example: f"Hello, {name}"

Starts/Ends With:
startswith() → Check if it starts with a substring.
endswith() → Check if it ends with a substring.

Check Content:
isalpha() → All characters are alphabetic.
isdigit() → All characters are digits.
isalnum() → Alphanumeric check.
isspace() → Check for whitespace.
isupper(), islower() → Case checks.

Reverse String:
Example: "Python"[::-1] → 'nohtyP'

--------------------NUMBER OPERATIONS-----------------------------

Basic Arithmetic:

- (Addition): 5 + 3 → 8

* (Subtraction): 5 - 3 → 2

- (Multiplication): 5 \* 3 → 15

/ (Division): 5 / 2 → 2.5

Floor Division:

//: 5 // 2 → 2

Modulus:

%: Remainder of division.
Example: 5 % 2 → 1

Exponentiation:

**: 2 ** 3 → 8

Absolute Value:

abs(): abs(-5) → 5

Rounding:

round(): Round to the nearest integer or specified decimal places.
Example: round(3.456, 2) → 3.46

Type Conversion:

int() → Convert to integer.

float() → Convert to float.

complex() → Convert to complex number.

Comparison Operators:

==, !=, <, >, <=, >=

Math Functions (from math module):

sqrt() → Square root.

pow() → Exponentiation.

sin(), cos(), tan() → Trigonometric functions.

log() → Logarithm.

ceil() and floor() → Round up or down.

factorial() → Compute factorial.

Random Numbers (from random module):

random() → Random float between 0 and 1.

randint(a, b) → Random integer between a and b.

choice() → Random selection from a sequence.

Bitwise Operations:

& (AND), | (OR), ^ (XOR), ~ (NOT)

Left Shift <<, Right Shift >>

Augmented Assignment:
Example: x += 5 (Same as x = x + 5)
