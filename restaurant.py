class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


# Create an instance
restaurant = Restaurant("Food Palace", "Italian")
restaurant2 = Restaurant("Spice Hub", "Indian")
restaurant3 = Restaurant("Burger Town", "Fast Food")

# Call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
# Call methods for each object
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()



