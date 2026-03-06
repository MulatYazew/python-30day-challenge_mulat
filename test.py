import json
from collections import Counter
import re
import string
import csv

#Exercises: Day 19
#Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder: a) Read obama_speech.txt file and count
# number of lines and words b) Read michelle_obama_speech.txt file and count number
# of lines and words c) Read donald_speech.txt file and count number of lines and words d)
# Read melina_trump_speech.txt file and count number of lines and words



#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    print(countries[0])

    language_counter = Counter()

    for country in countries:
        languages = country.get('languages', [])
        language_counter.update(languages)


    most_common = language_counter.most_common(top_n)
    return [(count, language) for language, count in most_common]


print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))