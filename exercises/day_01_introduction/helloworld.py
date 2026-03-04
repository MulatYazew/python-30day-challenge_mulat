import sys
import math

# Check the python version you are using
print("My Python version is:", sys.version)
# Open the python interactive shell and do the following operations. The operands are 3 and 4.
print(f"3+4={3+4}") # addition(+)
print(f"3-4={3-4}") #subtraction(-)
print(f"3*4={3*4}") #multiplication(*)
print(f"3%4={3%4}") #modulus(%)
print(f"3/4={3/4}") #division(/)
print(f"3**4={3**4}")   #exponential(**)
print(f"3//4={3//4}")   #floor division operator(//)
#Write strings on the python interactive shell. The strings are the following:
print("My name: Mulat Yazew") #Your name
print("My family name: Chekol") #Your family name
print("My country: Ethiopia")   #Your country
print("I am enjoying 30 days of python")#I am enjoying 30 days of python
#Check the data types of the following data:

print(type(10))     #10
print(type(9.8))    #9.8
print(type(3.14))    #3.14
print(type(4 - 4j))    #4 - 4j
print(type(['Asabeneh', 'Python', 'Finland']))  #['Asabeneh', 'Python', 'Finland']
print(type("Mulat"))    #Your name
print(type("Chekol"))   #Your family name
print(type("Ethiopia")) #Your country

#Find an Euclidean distance between (2, 3) and (10, 8)

x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The Euclidean distance between (2, 3) and (10, 8) is: {distance}")
