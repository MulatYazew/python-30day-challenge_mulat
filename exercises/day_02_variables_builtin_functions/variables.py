import math
#Exercises: Level 1
#Day 2: 30 Days of python programming
#Declare a first name variable and assign a value to it
first_name = "Mulat"
#Declare a last name variable and assign a value to it
last_name = "Chekol"
#Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
#Declare a country variable and assign a value to it
country = "Ethiopia"
#Declare a city variable and assign a value to it
city = "Addis Ababa"
#Declare an age variable and assign a value to it
age = 29
#Declare a year variable and assign a value to it
year = 2026
#Declare a variable is_married and assign a value to it
is_married = False
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light_on = False
#Declare multiple variable on one line
name, age, country = "Mulat", 29, "Ethiopia"
#Exercises: Level 2
#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
#Using the len() built-in function, find the length of your first name
print(len(first_name))
#Compare the length of your first name and your last name
print(len(first_name) == len(last_name))
#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
#The radius of a circle is 30 meters.
radius = 30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi * radius ** 2
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius
#Take radius as user input and calculate the area.
radius_input = float(input("Enter the radius of the circle: "))
area_of_new_circle = math.pi * radius_input ** 2
print("The area of the circle with radius", radius_input, "is", area_of_new_circle)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name_input = input("Enter your first name:")
last_name_input = input("Enter your last name:")
country_input = input("Enter your country:")
age_input = int(input("Enter your age:"))
print("Your name is", first_name_input, last_name_input, "and you are from", country_input, "and you are", age_input, "years old.")
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')