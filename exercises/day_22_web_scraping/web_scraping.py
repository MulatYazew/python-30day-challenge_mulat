import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd
#1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

def regex_function(text):
    # Use regex to extract key-value pairs
    match = re.search(r"(\D+)([\d,]+.*)", text)
    if match:
        key = match.group(1).strip()
        value = match.group(2).strip()
        return key, value
    return None, None
def scrape_bu_facts_stats():
    url = "http://www.bu.edu/president/boston-university-facts-stats/"
    response = requests.get(url)
    response.raise_for_status()

    # Use the robust HTML parser
    soup = BeautifulSoup(response.text, "lxml")

    data = {}

    # -- Quick Facts & Stats (top-level stats) --
    # Research Expenditures, Study Abroad Programs, Sponsored Research Awards
    quick_facts_and_stats = soup.find("h4", string=lambda text: text and "Quick Facts & Stats" in text)
    if quick_facts_and_stats:
        quick_facts = {}
        for num in quick_facts_and_stats.find_next_sibling("div"):
            text = num.get_text(strip=True)
            key_value = regex_function(text)
            if key_value is None:
                continue  # skip if regex returned nothing
            
            key, value = key_value
            
            # Skip adding to dict if value is None or empty
            if value:
                quick_facts[key] = value

        data["Quick Facts & Stats"] = quick_facts

    # -- Community Statistics (list items under community heading) --
    community_section = soup.find("h4", string=lambda text: text and "Community" in text)
    if community_section:
        community = {}
        for li in community_section.find_next_sibling("ul").find_all("li"):
            text = li.get_text(strip=True)
            key, value = regex_function(text)

            community[key] = value
        data["Community"] = community

    # -- Campus Statistics (each under its own h4 heading) --
    campus_section = soup.find("h4", string=lambda text: text and "Campus" in text)
    if campus_section:
        campus = {}
        for field in campus_section.find_next_sibling("div"):
            text = field.get_text(strip=True)

            key_value = regex_function(text)
            if key_value is None:
                continue  # skip if regex returned nothing
            
            key, value = key_value
            
            # Skip adding to dict if value is None or empty
            if value:
                campus[key] = value
            
        data["Campus"] = campus

    # -- Academics Statistics (list items under academics heading) --
    academics_section = soup.find("h4", string=lambda text: text and "Academics" in text)
    if academics_section:
        academics = {}
        for li in academics_section.find_next_sibling("ul").find_all("li"):
            text = li.get_text(strip=True)
            key, value = regex_function(text)
        
            academics[key] = value
        data["Academics"] = academics

    # Save to JSON file
    file_path = "./data/bu_facts_stats.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved BU Facts & Stats to {file_path}")




#2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

def extract_table():
    
    url = "https://archive.ics.uci.edu/ml/datasets"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

        # Find the table by its class name
    table = soup.find("table", {"border": "1"})
    if not table:
        print("Table not found on the page.")
        return
    # Extract headers
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    # Extract rows
    rows = []
    for tr in table.find_all("tr")[1:]:  # Skip header row
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if cells:
            rows.append(cells)
    # Create a DataFrame and save as JSON
    df = pd.DataFrame(rows, columns=headers)
    df.to_json("./data/uci_datasets.json", orient="records", indent=2)
    print("Successfully saved UCI datasets to ./data/uci_datasets.json")
    

#3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
# The table is not very structured and the scrapping may take very long time.

def main():
   scrape_bu_facts_stats()
   




if __name__ == "__main__":
    main()

    extract_table()