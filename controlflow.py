#intoduction to control flow statements in python
#control flow statements are used to control the flow of execution of a program
#there are three types of control flow statements in python:
#1. Conditional statements (if, elif, else)#selective execution
#2. Loop statements (for, while)
#3. Jump statements (break, continue, pass)
# #Sequential
# Functions#modular
# switch case statements#not available in python     


#1. Conditional statements (if, elif, else)
#allow us to execute a block of code based on a condition
#used to implement business rules and decision making in a program
#handles different user inputs and scenarios
#create intelligent programs that can adapt to different situations
"""""
x=int(input("Enter a number: "))   
if x>0:
    print("x is a positive number") #indented needed to indicate that this block of code belongs to the if statement
#elif x>=0:
   # print("x is a non negative number")#another if condition to check if x is a non negative number
elif x==0:
    print("x is zero") #while if checks if true, elif is executed when the previous condition is false and the current condition is true
else:
    print("x is a negative number") #while if checks if true, else is executed when all the previous conditions are false
"""
    #lab activity:takes students score as input and assigns grade based on folloing criteria;
#90-100 A
#80-89 B    
#70-79 C
#60-69 D    
#below 60 F
score=int(input("Enter your score: "))
if score>=90:
    grade="A"
    message="Excellent"
elif score>=80:
    grade="B"
    message="Good"
elif score>=70:
    grade="C"
    message="Satisfactory"
elif score>=60:
    grade="D"
    message="Needs Improvement"
else:
    grade="F"
    message="Failed"
print(f"Your grade is: {grade}")
print(f" {message}")
#kinds of errors in python
#1. Syntax errors: occur when the code is not written in the correct syntax of the
#programming language. For example, missing a colon at the end of an if statement or using incorrect indentation.
#2. Runtime errors: occur when the code is syntactically correct but encounters an error
#during execution. For example, dividing by zero or trying to access an index that is out of range in a list.
#3. Logical errors: occur when the code runs without any syntax or runtime errors but produces
#incorrect results. For example, using the wrong operator in a calculation or implementing an incorrect algorithm.
#4. Name errors: occur when a variable or function is referenced before it is defined. For example, trying to use a variable that has not been assigned a value or calling a function that has not been defined.

