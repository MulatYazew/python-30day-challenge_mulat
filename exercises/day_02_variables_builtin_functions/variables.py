# Exercises: Level 1
# Declare a first name variable and assign a value to it
first_name = 'Antonio'
# Declare a last name variable and assign a value to it
last_name = 'Gutierrez'
# Declare a full name variable and assign a value to it
full_name = "Antonio Gutierrez"
# Declare a country variable and assign a value to it
country = 'Mexico'
# Declare a city variable and assign a value to it
city = 'Mexico City'
# Declare an age variable and assign a value to it
age = 60
# Declare a year variable and assign a value to it
year = 2026
# Declare a variable is_married and assign a value to it
is_married = True
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = False
# Declare multiple variables on one line
first_name, last_name, country, age = 'Antonio', 'Gutierrez', 'Mexico', 60

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))  # <class 'str'>
print(type(last_name))   # <class 'str'>
print(type(full_name))   # <class 'str'>
print(type(country))     # <class 'str'>
print(type(city))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(year))        # <class 'int'>
print(type(is_married))  # <class 'bool'>
print(type(is_true))     # <class 'bool'>
print(type(is_light_on)) # <class 'bool'>


print(len(first_name))  # Length of first name
print(len(first_name) > len(last_name))  # Compare length of first name and last name

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
radius = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * radius ** 2
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius


# Take radius as user input and calculate the area.
radius = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print(f"The area of the circle with radius {radius} is: {area_of_circle}")
print(f"The circumference of the circle with radius {radius} is: {circum_of_circle}")