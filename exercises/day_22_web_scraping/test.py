import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the UCI datasets index page
url = 'https://archive.ics.uci.edu/datasets'

# Send a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing dataset information
table = soup.find('table', {'cellpadding': '3'})

# Initialize lists to store extracted data
dataset_names = []
dataset_links = []

# Check if the table was found before processing
if table:
    # Iterate over each row in the table (skipping the header row)
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) > 1 and cols[0].find('a'):
            name = cols[0].get_text(strip=True)
            link = 'https://archive.ics.uci.edu' + cols[0].find('a')['href']
            dataset_names.append(name)
            dataset_links.append(link)
else:
    print("Dataset table not found on the page.")

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'Dataset Name': dataset_names,
    'URL': dataset_links
})

# Convert the DataFrame to JSON format
json_data = df.to_json(orient='records', lines=True)

# Save the JSON data to a file
with open('uci_datasets.json', 'w') as f:
    f.write(json_data)

print("JSON file 'uci_datasets.json' has been created.")
