import math
#1. Declare your age as integer variable
age = 29
#2. Declare your height as a float variable
height = 1.70
#3. Declare a variable that store a complex number
complex_number = 2 + 3j
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
 #   Enter base: 20
base_triangle = float(input("Enter base: "))
#    Enter height: 10
height_triangle = float(input("Enter height: "))
 #   The area of the triangle is 100
area_triangle = 0.5 * base_triangle * height_triangle
print("The area of the triangle is", area_triangle)
#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
#Enter side a: 5
a = float(input("Enter side a: "))
#Enter side b: 4
b = float(input("Enter side b: "))
#Enter side c: 3
c = float(input("Enter side c: "))
#The perimeter of the triangle is 12
perimeter_triangle  = a + b + c
print("The perimeter of the triangle is", perimeter_triangle)
#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
legnth_rectangle = float(input("Enter length of the rectangle: "))
width_rectangle = float(input("Enter width of the rectangle: "))
area_rectangle = legnth_rectangle * width_rectangle
perimeter_rectangle = 2 * (legnth_rectangle + width_rectangle)
print("The area of the rectangle is", area_rectangle)
print("The perimeter of the rectangle is", perimeter_rectangle)
#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius_circle = float(input("Enter radius of the circle: "))
pi = math.pi
area_circle = pi * radius_circle * radius_circle
circumference_circle = 2 * pi * radius_circle
print("The area of the circle is", area_circle)
print("The circumference of the circle is", circumference_circle)
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
## take two points from the line and use the formula to calculate the slope, x-intercept and y-intercept
x1_8, y1_8 = 0, -2 
x2_8, y2_8 = 1, 0
slope_8  = (y2_8 - y1_8) / (x2_8 - x1_8)
x_intercept_8 = -x1_8 / slope_8
y_intercept_8 = y1_8 - slope_8 * x1_8
print("The slope of the line is", slope_8)
print("The x-intercept of the line is", x_intercept_8)
print("The y-intercept of the line is", y_intercept_8)
#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1_9, y1_9 = 2, 2
x2_9, y2_9 = 6, 10
slope_9 = (y2_9 - y1_9) / (x2_9 - x1_9)
distance = math.sqrt((x2_9 - x1_9) ** 2 + (y2_9 - y1_9) ** 2)
#10. Compare the slopes in tasks 8 and 9.
print(slope_8 == slope_9)

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x1 = (-6-math.sqrt(6**2 - 4*1*9)) / (2*1)
x2 = (-6+math.sqrt(6**2 - 4*1*9)) / (2*1)
print("The value of x when y is 0 is", x1, "or", x2)

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('dragon'))
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')
#13. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in "I hope this course is not full of jargon")
#14. There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')
#15. Find the length of the text python and convert the value to float and convert it to string
length_python = len('python')
length_python_float = float(length_python)
length_python_str = str(length_python_float)
print(length_python_str)
#16. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:    print(number, "is an odd number.")
#17. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))
#19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))
#20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)
#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is", weekly_earning)
#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
years_lived = float(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds.")
#23. Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
