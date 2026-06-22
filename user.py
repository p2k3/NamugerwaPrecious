class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print("User Information")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome.")


# Create users
user1 = User("John", "Doe", 25, "john@gmail.com")
user2 = User("Mary", "Smith", 30, "mary@gmail.com")
user3 = User("Peter", "Jones", 22, "peter@gmail.com")

# Call methods
user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()