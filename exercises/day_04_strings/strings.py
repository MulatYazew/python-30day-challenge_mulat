#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
python_string = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(python_string)
#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding_string = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(coding_string)
#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#4. Print the variable company using print().
print(company)
#5. Print the length of the company string using len() method and print().
print(len(company))
#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())
#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())
#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9. Cut(slice) out the first word of Coding For All string.
print(company[7:])
#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
#12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
python_for_everyone = "Python for Everyone"
print(python_for_everyone.replace('Everyone', 'All'))
#13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(','))
#15. What is the character at index 0 in the string Coding For All.
print(company[0])
#16. What is the last index of the string Coding For All.
print(len(company) - 1)
#17. What character is at index 10 in "Coding For All" string.
print(company[10])
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_for_everyone = "Python For Everyone"
acronym1= python_for_everyone[0] + "." + python_for_everyone[7]+ "." + python_for_everyone[11]
print(acronym1)
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
acronym2 = company[0] + "." + company[7]+ "." + company[11]
print(acronym2)
#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find('C'))
#21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find('F'))
#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):sentence.rfind('because') + len('because')])
#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):sentence.rfind('because') + len('because')])
#28. Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
#29. Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))
#30. '   Coding For All      '  , remove the left trailing spaces in the given string.
print('   Coding For All      '.lstrip())
#31. '   Coding For All      '  , remove the right trailing spaces in the
print('   Coding For All      '.rstrip())
#32. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())
#33. Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#34. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_libraries))
#35. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

#36. Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")
#37. Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#38. Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")