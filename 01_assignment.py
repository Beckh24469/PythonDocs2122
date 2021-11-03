# Beckham
# Assignment Examples

# You can assign "values" to "variables" by using and equals (right side goes into left side)
x = 5

# When python reads a variable name, it relaces it with the variable's stored value
y = x + 5

# There are four different primitive datatypes

# Integers: any WHOLE number, positive or negative
age = 16
# Float: any number with a decimal, positive or negative
grade = 98.6

# String:a string of human-readable characters
name = "Beckham"
# numbers in a string are not bumbers, they are letters
favoriteNumber = "69"

# Boolean: True or False
# True is any value that is not false or empty
isSmart = True

# You can output to the consoole by using 'print()'
print(age)
print(grade)
print(name)
print(isSmart)
print(favoriteNumber)

# You can concatenate values together
print("My name is " + name)
# You can use functions to convert datatypes
print("and my age is " + str(age))
# Don't forget! If you convert a value permanently, you must assign the converted value into a variable
age = str(age)
# You can convert back and forth with int(), str(), bool(), and float()
print(int(age))
print(float(age))
print(bool(age))
