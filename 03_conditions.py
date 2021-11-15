# Beckham Phillips
# Practice using expressions and conditional statements

# An expression is a problem that must be solved
# 5 + 5 is an "arithmetic" expression
x = 2 + 3

# Functions/methods must be resolved as expressions as well
answer = input("What is your name?")
age = input("How old are you?")
age = int(age)

# Comparison expression resolve as True/False
print( 7 > 7 )
print( 7 >= 7 )
print( x == 10)
print( x > 10 or x < 10 )

# A conditional statement runs if its condition is True / not False
if answer == "Bob":
    print("Hello, Bob! Welcome Back!")
    print("This line also prints if your name is Bob")
elif answer == "Vadim":
    print("Hey! You still owe me money!")
else:
    print("Sorry, I only talk to Bob")
print("This line isn't inside of the if statement, and prints regardless")

if age >= 10:
    print("Here is your license")
elif age == 9:
    print("You still have one year to go!")
else:
    print("You are too young")

# ^ If checks a condition
# ^ Elif checks a condition if the previous conditions were not true
# ^ You can have as many elif's as you want
# ^ Else runs if no prior conditions were true
