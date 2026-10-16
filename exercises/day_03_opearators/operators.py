"""
Exercises: Day 3 - Operators
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    Enter side a: 5
    Enter side b: 4
    Enter side c: 3
    The perimeter of the triangle is 12
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text python and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    Enter number of years you have lived: 100
    You have lived for 3153600000 seconds.
23. Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
# Declare your age as integer variable
age = 29
# Declare your height as a float variable
height = 1.70
# Declare a variable that store a complex number
complex_number = 2 + 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius of the circle: "))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x1, y1 = 0, -2  # y-intercept
x2, y2 = 1, 0   # x-intercept
slope = (y2 - y1) / (x2 - x1)
print(f"The slope of the line y = 2x - 2 is {slope}")
print(f"The x-intercept is at ({x2}, {y2})")
print(f"The y-intercept is at ({x1}, {y1})")
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"The slope is {slope}")
print(f"The Euclidean distance between points (2, 2) and (6, 10) is {distance}")

# Compare the slopes in tasks 8 and 9.
# The slope from task 8 is 2, and the slope from task 9 is 2 as well, so they are equal.

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def calculate_y(x):
    return x ** 2 + 6 * x + 9

calculate_y_values = [calculate_y(x) for x in range(-10, 11)]
zero_y_values = [x for x in range(-10, 11) if calculate_y(x) == 0]
print(f"Values of y for x in range -10 to 10: {calculate_y_values}")
print(f"The x values where y is 0: {zero_y_values}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python')
length_dragon = len('dragon')
falsy_comparison = length_python > length_dragon
print(f"Length of 'python': {length_python}, Length of 'dragon': {length_dragon}, Falsy comparison (python > dragon): {falsy_comparison}")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
on_in_python = 'on' in 'python'
on_in_dragon = 'on' in 'dragon'
both_on = on_in_python and on_in_dragon
print(f"'on' in 'python': {on_in_python}, 'on' in 'dragon': {on_in_dragon}, Both contain 'on': {both_on}")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
jargon_in_sentence = 'jargon' in sentence
print(f"'jargon' in sentence: {jargon_in_sentence}")

# There is no 'on' in both dragon and python
no_on_in_both = 'on' not in 'dragon' and 'on' not in 'python'
print(f"There is no 'on' in both dragon and python: {no_on_in_both}")

# Find the length of the text python and convert the value to float and convert it to string
length_python = len('python')
length_python_float = float(length_python)
length_python_str = str(length_python_float)
print(f"Length of 'python': {length_python}, as float: {length_python_float}, as string: {length_python_str}")

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def is_even(number):
    return number % 2 == 0

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_value = int(2.7)
floor_division_check = floor_division == int_value
print(f"Floor division of 7 by 3: {floor_division}, int(2.7): {int_value}, Are they equal: {floor_division_check}")

# Check if type of '10' is equal to type of 10
type_check = type('10') == type(10)
print(f"Type of '10': {type('10')}, Type of 10: {type(10)}, Are they equal: {type_check}")

# Check if int('9.8') is equal to 10
int_check = int(float('9.8')) == 10
print(f"int('9.8') == 10: {int_check}")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours:"))
rate_per_hour = float(input("Enter rate per hour:"))
pay = hours * rate_per_hour
print(f"Your weekly earning is {pay}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_in_a_year
print(f"You have lived for {total_seconds} seconds.")

# Write a Python script that displays the following table
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)

