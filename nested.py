#what is a nested condition?
#A nested condition is a condition that is contained within another condition.
#    It allows us to check multiple conditions in a hierarchical manner.
#Nested conditions are useful when we want to check for multiple conditions that are related to each other.
#For example, we can use a nested condition to check if a number is positive, negative, or zero.
#labactivity
#write a program for a login authentication that takes username and checks password if password is coreect you have logged in succesfully otherwise you have entered an incorrect password if username is not correct you have entered an incorrect username
username=input("Enter your username: ")
password=input("Enter your password: ")
users={"precious": "password1", "john": "password2", "mary": "password3"}
#check if username exists
if username in users:
    #check if password is correct
    if password==users[username]:
        print("You have logged in successfully")
    else:
        print("You have entered an incorrect password")
else:
    print("You have entered an incorrect username")