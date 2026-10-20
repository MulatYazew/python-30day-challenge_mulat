# Exercises: Level 1
#1. Declare an empty list
empty_list = []

#2. Declare a list with more than 5 items
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']

#3. Find the length of your list
print(len(fruits))

#4. Get the first item, the middle item and the last item of the list
print(fruits[0])  # First item
print(fruits[len(fruits)//2])  # Middle item
print(fruits[-1])  # Last item

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John', 25, 5.8, 'Single', '123 Main St']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0])  # First company
print(it_companies[len(it_companies)//2])  # Middle company
print(it_companies[-1])  # Last company

#10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append('Tesla')

#12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Apple')

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[5] = it_companies[5].upper()

#14.Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

#15. Check if a certain company exists in the it_companies list
company_to_check = 'Tesla'
if company_to_check in it_companies:
    print(f"{company_to_check} exists in the list.")
else:
    print(f"{company_to_check} does not exist in the list.")

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17.Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#18. Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]

#19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]

#20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = [it_companies[middle_index]]

#21. Remove the first IT company from the list
it_companies.pop(0)

#22. Remove the middle IT company or companies from the list
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]
else:
    del it_companies[middle_index]

#23. Remove the last IT company from the list
it_companies.pop()

#24. Remove all IT companies from the list
it_companies.clear()  

#25. Destroy the IT companies list
del it_companies

# Exercises: Level 2
#26. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
# Add the min age and the max age again to the list
ages.append(max_age)
ages.append(min_age)
# Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 0:
    median_age = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
else:
    median_age = ages[len(ages)//2]
print(median_age)
# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age)
# Find the range of the ages (max minus min)
range_ages = max_age - min_age
# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(min_diff)
print(max_diff)
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]
print(first_half)
print(second_half)
# Unpack the first three countries and the rest as scandic countries.
country1, country2, country3, *scandic_countries = countries
print(country1)
print(country2)
print(country3)
print(scandic_countries)