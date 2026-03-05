#Exercises: Day 8


#Create an empty dictionary called dog

dct = {}
#Add name, color, breed, legs, age to the dog dictionary
dct['name'] = 'Rex'
dct['color'] = 'Brown'
dct['breed'] = 'Labrador'
dct['legs'] = 4
dct['age'] = 5
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis', 'Machine Learning', 'Deep Learning', 'Natural Language Processing', 'Computer Vision', 'Big Data'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
    }
#Get the length of the student dictionary
length = len(student)
print(length)
#Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
#Modify the skills values by adding one or two skills
student['skills'].append('Cloud Computing')
student['skills'].append('DevOps')
print(student['skills'])
#Get the dictionary keys as a list
print(list(student.keys()))
#Get the dictionary values as a list
print(list(student.values()))
#Change the dictionary to a list of tuples using items() method
print(list(student.items()))
#Delete one of the items in the dictionary
del student['marital_status']
print(student)
#Delete one of the dictionaries
del student