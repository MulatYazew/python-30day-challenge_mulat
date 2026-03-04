# Exercises: Level 1
#Declare an empty list
empty_list = []

#Declare a list with more than 5 items
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

#Find the length of your list
print(len(my_list))

#Get the first item, the middle item and the last item of the list
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]
print(f"First item: {first_item}, Middle item: {middle_item}, Last item: {last_item}")

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John Doe', 30, 5.9, 'Single', 'Via Gustavo Modena, 36, 20129 Milan, Italy']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(f"First company: {first_company}, Middle company: {middle_company}, Last company: {last_company}")

#Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Netflix')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

#Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

#Check if a certain company exists in the it_companies list.
print('Google' in it_companies)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()

#Slice out the first 3 companies from the list
it_companies[:3]

#Slice out the last 3 companies from the list
it_companies[-3:]

#Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:    middle_companies = it_companies[middle_index:middle_index + 1]

#Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]
else:    del it_companies[middle_index]

#Remove the last IT company from the list
it_companies.pop(-1)

#Remove all IT companies from the list
it_companies.clear()
print('After clearing:', it_companies)

#Destroy the IT companies list
del it_companies

#Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

deveops = front_end + back_end
print(deveops)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = deveops.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)
# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f"Min age: {min_age}, Max age: {max_age}")
#Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)
#Find the median age (one middle item or two middle items divided by two)
ages.sort()
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:    median_age = ages[n // 2]
print(f"Median age: {median_age}")
#Find the range of the ages (max minus min)
age_range = max_age - min_age
#Compare the value of (min - average) and (max - average), use abs() method
average_age = sum(ages) / len(ages)
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(f"Min - Average: {min_diff}, Max - Average: {max_diff}")
print('_' * 50)
#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
countries.sort()
n = len(countries)
if n % 2 == 0:
    middle_countries = countries[n // 2 - 1:n // 2 + 1]
else:    middle_countries = countries[n // 2]
print(f"Middle country(ies): {middle_countries}")

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries.sort()
n = len(countries)
if n % 2 == 0:
    first_half = countries[:n // 2]
    second_half = countries[n // 2:]
else:    
    first_half = countries[:n // 2 + 1]
    second_half = countries[n // 2 + 1:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries
print(f"First three countries: {first}, {second}, {third}")
print(f"Scandic countries: {scandic_countries}")