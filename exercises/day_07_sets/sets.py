#Exercises: Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
#Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'TikTok'])
#Remove one of the companies from the set it_companies
it_companies.remove('IBM')
#What is the difference between remove and discard
"""
The remove() method removes the specified element from the set. If the element is not found, it raises a KeyError. 
On the other hand, the discard() method also removes the specified element from the set, but if the element is not found, 
it does not raise an error and simply does nothing.
In summary, the main difference is that remove() will raise an error if the element is not present in the set, while discard() will not.
"""
# Exercises: Level 2
#Join A and B
C = A.union(B)
#Find A intersection B
D = A.intersection(B)
#Is A subset of B
is_subset = A.issubset(B)
#Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
#Join A with B and B with A
E = A.union(B)
F = B.union(A)
#What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
#Delete the sets completely
del A
#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age) == len(age_set))
#Explain the difference between the following data types: string, list, tuple and set
"""
- String: A string is a sequence of characters enclosed in quotes. It is immutable, meaning it cannot be changed after it is created. 
    Example: "Hello, World!" 
- List: A list is an ordered collection of items that can be of different types. It is mutable, meaning it can be changed after it is created. 
    Example: [1, 2, 3, 'Hello', True]
- Tuple: A tuple is similar to a list but is immutable. It is an ordered collection of items that can be of different types. 
    Example: (1, 2, 3, 'Hello', True)
- Set: A set is an unordered collection of unique items. It is mutable, meaning it can be changed after it is created. 
    Example: {1, 2, 3, 'Hello', True}
"""
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
