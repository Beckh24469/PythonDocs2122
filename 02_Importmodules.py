# import the basics module to use its code
import basics

# make a new application project from the basics module
app = basics.newProgram()

# use a method that belongs to our new application object
app.print('yo momma')

# print a property of our new application object
app.print( app.debugging )

# This line won't print if app.debugging is False
app.debug("Hello")

# we'llenable for the application
app.debugging = True
app.debug('Now it works!')

# import a default python module
import random

# use a method from the random moodule
randomNumber = random.randint(1, 10)
app.print(randomNumber)
