import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Read the hacker_news.csv file from data directory

df = pd.read_csv('./data/hacker_news.csv')

#Get the first five rows
print(df.head(5))
#Get the last five rows
print(df.tail(5))
#Get the title column as pandas series
print(df['title'])
#Get the title column as list
print(df['title'].tolist())
#Get the title column as numpy array
print(df['title'].values)
#Get the number of rows and columns
print(df.shape[0]) # number of rows
print(df.shape[1]) # number of columns
#Filter the titles which contain python

#Count the number of rows and columns
print(df.shape)
#Filter the titles which contain python
python_titles = df[df['title'].str.contains('python', case=False, na=False)]
print(python_titles)
#Filter the titles which contain JavaScript
javascript_titles = df[df['title'].str.contains('javascript', case=False, na=False)]
print(javascript_titles)
#Explore the data and make sense of it

