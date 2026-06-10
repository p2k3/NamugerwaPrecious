#switch case statements are not available in python but we can use case statements to achieve similar functionality
"""light_color=input("Enter the traffic light color (red, yellow, green): ") #looks at one case at a time

match light_color:
    case "red":
        print("Stop")
    case "yellow":
        print("Prepare to stop")
    case "green":
        print("Go")
    case _:
        print("Invalid color")"""
       
        #write a program that uses switch case statements to determine the day of the week based on a number input (1-7) where 1 is Monday and 7 is Sunday
day_number=int(input("Enter a number (1-7) to determine the day of the week: "))
match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number. Please enter a number between 1 and 7.")