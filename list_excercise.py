# Creating a list of names
names = ["John", "Mary", "Peter", "Jane", "Paul"]

# Output the 2nd item (index 1)
print(names[1])  # Output: Mary

names = ["John", "Mary", "Peter", "Jane", "Paul"]

# Change first item
names[0] = "David"
print(names)  # Output: ['David', 'Mary', 'Peter', 'Jane', 'Paul']

#adding new item to list
names.append("Lucy")
print(names)  # Output: ['David', 'Mary', 'Peter', 'Jane', 'Paul', 'Lucy']

names = ["John", "Mary", "Peter", "Jane", "Paul"]

# Insert at position 2 (third position)
names.insert(2, "Bathel")
print(names)  # Output: ['John', 'Mary', 'Bathel', 'Peter', 'Jane', 'Paul']

names = ["John", "Mary", "Bathel", "Peter", "Jane", "Paul"]

# Remove item at index 3 (4th position)
names.pop(3)
print(names)  # Output: ['John', 'Mary', 'Bathel', 'Jane', 'Paul']
names = ["John", "Mary", "Bathel", "Jane", "Paul"]

# Negative indexing: -1 is the last item
print(names[-1])  # Output: Paul

# List with 7 items
cities = ["Kampala", "Nairobi", "Lagos", "Cairo", "Cape Town", "Accra", "Dubai"]

# Print 3rd, 4th, 5th items (indices 2, 3, 4)
print(cities[2:5])  # Output: ['Lagos', 'Cairo', 'Cape Town']
#extracts elements from start index up to 4 ( not including) end index.

# Original list
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]

# Make a copy
countries_copy = countries.copy()
print(countries_copy)  # Output: ['Uganda', 'Kenya', 'Tanzania', 'Rwanda', 'Burundi']

countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]

# Loop through using for loop
for country in countries:
    print(country)

    animals = ["lion", "elephant", "giraffe", "zebra", "hippo"]

# Sort ascending (A to Z)
animals.sort()
print("Ascending:", animals)  # Output: ['elephant', 'giraffe', 'hippo', 'lion', 'zebra']

# Sort descending (Z to A)
animals.sort(reverse=True)
print("Descending:", animals)  # Output: ['zebra', 'lion', 'hippo', 'giraffe', 'elephant']

animals = ["lion", "elephant", "giraffe", "zebra", "hippo"]



# Check each animal for letter 'a'
for animal in animals:
    if 'a' in animal:
        print(animal)  # Output: elephant, giraffe, zebra

        first_names = ["John", "Mary", "Peter"]
last_names = ["Doe", "Smith", "Jones"]

# Join using + operator
full_names = first_names + last_names
print(full_names)  # Output: ['John', 'Mary', 'Peter', 'Doe', 'Smith', 'Jones']