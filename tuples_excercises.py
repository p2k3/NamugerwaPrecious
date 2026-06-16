# 1. Output favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])

# 2. Use negative indexing to print the 2nd last item
x = ("samsung", "iphone", "tecno", "redmi")
print(x[-2])

# 3. Update "iphone" to "itel"
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

# 4. Add "Huawei" to your tuple
x = ("samsung", "itel", "tecno", "redmi")
x_list = list(x)
x_list.append("Huawei")
x = tuple(x_list)
print(x)

# 5. Loop through the tuple
x = ("samsung", "itel", "tecno", "redmi", "Huawei")
for phone in x:
    print(phone)

# 6. Remove/delete the first item in your tuple
x = ("samsung", "itel", "tecno", "redmi", "Huawei")
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print(x)

# 7. Using tuple() constructor, create a tuple of the cities in Uganda
ugandan_cities = tuple(["Kampala", "Jinja", "Entebbe", "Mbarara", "Gulu"])
print(ugandan_cities)

# 8. Unpack your tuple
cities = ("Kampala", "Jinja", "Entebbe")
city1, city2, city3 = cities
print(city1)
print(city2)
print(city3)

# 9. Use range of indexes to print 2nd, 3rd, 4th cities
cities = ("Kampala", "Jinja", "Entebbe", "Mbarara", "Gulu")
print(cities[1:4])

# 10. Join two tuples
first_names = ("John", "Mary", "Peter")
last_names = ("Doe", "Smith", "Jones")
full_names = first_names + last_names
print(full_names)

# 11. Create a tuple of colors and multiply by 3
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print(colors_multiplied)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print(count)