#  Exercises: Level 1
#Create an empty tuple
empty_tuple = ()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Asrat', 'Belayneh', 'Habtamu')
sisters = ('Emebet', 'Banchi', 'Werknesh')
#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
#How many siblings do you have?
num_siblings = len(siblings)
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Yazew', 'Azeneg')
#Exercises: Level 2

#Unpack siblings and parents from family_members
brother1, brother2, brother3, sister1, sister2, sister3, father, mother = family_members
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt') 
food_stuff_tp = fruits + vegetables + animal_products

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle_items = food_stuff_tp[middle_index - 1: middle_index + 1]
else:    middle_items = food_stuff_tp[middle_index]
#Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
#Delete the food_stuff_tp tuple completely
del food_stuff_tp
#Check if an item exists in tuple:
print('milk' in food_stuff_lt)  # True
print('meat' in food_stuff_lt)  # False
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True