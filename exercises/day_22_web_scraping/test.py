import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = {}

# Extract all list items (stats on the page)
for li in soup.find_all("li"):
    text = li.get_text(strip=True)
    
    # Split key and value
    parts = text.rsplit(" ", 1)
    if len(parts) == 2:
        key, value = parts
        data[key] = value
    else:
        data[text] = None

# Extract main stat blocks (like Research Expenditures etc.)
headers = soup.find_all(["h2","h3","h4"])
for header in headers:
    next_tag = header.find_next()
    if next_tag and next_tag.name == "p":
        data[header.text.strip()] = next_tag.text.strip()

# Save as JSON
with open("./data/bu_stats.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data saved to bu_stats.json")