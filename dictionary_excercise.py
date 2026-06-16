# 1. Print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["brand"] = "Adidas"
print(Shoes)

# 3. Add a key/value pair "type": "sneakers"
Shoes = {
    "brand": "Adidas",
    "color": "black",
    "size": 40
}
Shoes["type"] = "sneakers"
print(Shoes)

# 4. Return a list of all the keys
Shoes = {
    "brand": "Adidas",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}
keys = Shoes.keys()
print(keys)

# 5. Return a list of all the values
Shoes = {
    "brand": "Adidas",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}
values = Shoes.values()
print(values)

# 6. Check if key "size" exists
Shoes = {
    "brand": "Adidas",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}
if "size" in Shoes:
    print("Size exists in the dictionary")
else:
    print("Size does not exist")

# 7. Loop through the dictionary
Shoes = {
    "brand": "Adidas",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}
for key, value in Shoes.items():
    print(f"{key}: {value}")

# 8. Remove "color" from the dictionary
Shoes = {
    "brand": "Adidas",
    "color": "black",
    "size": 40,
    "type": "sneakers"
}
del Shoes["color"]
print(Shoes)

# 9. Empty the dictionary
Shoes = {
    "brand": "Adidas",
    "size": 40,
    "type": "sneakers"
}
Shoes.clear()
print(Shoes)

# 10. Make a copy of a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "Kampala"
}
person_copy = person.copy()
print(person_copy)

# 11. Show nested dictionaries
students = {
    "student1": {
        "name": "John",
        "age": 20,
        "course": "Computer Science"
    },
    "student2": {
        "name": "Mary",
        "age": 22,
        "course": "Engineering"
    }
}
print(students["student1"]["name"])
print(students["student2"]["course"])
for student_id, details in students.items():
    print(f"{student_id}:")
    for key, value in details.items():
        print(f"  {key}: {value}")