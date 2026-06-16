# 1. Concatenate integer and string
age = 25
name = "John"
result = name + " is " + str(age) + " years old"
print(result)

# 2. Output string without spaces
txt = "      Hello,       Uganda!       "
cleaned_txt = txt.replace(" ", "")
print(cleaned_txt)

# 3. Convert txt to uppercase
txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print(uppercase_txt)

# 4. Replace character 'U' with 'V'
txt = "Hello, Uganda!"
replaced_txt = txt.replace("U", "V")
print(replaced_txt)

# 5. Return characters in 2nd, 3rd, 4th position
y = "I am proudly Ugandan"
print(y[1:4])

# 6. Correct the string error
# Method 1: Use single quotes for the outer string
x = 'All "Data Scientists" are cool!'
print(x)

# Method 2: Escape the inner quotes
x = "All \"Data Scientists\" are cool!"
print(x)