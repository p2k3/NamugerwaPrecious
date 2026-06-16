# 1. Use set() constructor to create a set of 3 favorite beverages
beverages = set(["coffee", "tea", "juice"])
print(beverages)

# 2. Add 2 more items to the beverages set
beverages = {"coffee", "tea", "juice"}
beverages.add("milk")
beverages.add("water")
print(beverages)

# 3. Check if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present")

# 4. Remove "kettle" from the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)

# 5. Loop through the set
mySet = {"oven", "microwave", "refrigerator"}
for item in mySet:
    print(item)

# 6. Add elements in list to elements in set
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["kiwi", "lemon"]
my_set.update(my_list)
print(my_set)

# 7. Join two sets
ages = {25, 30, 35}
names = {"John", "Mary", "Peter"}
combined_set = ages.union(names)
print(combined_set)