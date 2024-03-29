import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://shadowfox.in/"
json_file_path = "intermediate/webscraper.json"

# Check if the JSON file already exists
if os.path.exists(json_file_path):
    # Load existing data from the JSON file
    with open(json_file_path, "r") as json_file:
        existing_data = json.load(json_file)
else:
    existing_data = {}

try:
    # Sending a GET request to the URL
    page = requests.get(url)

    # Checking if the request was successful
    if page.status_code == 200:
        # Parsing the HTML content
        soup = BeautifulSoup(page.text, "html.parser")

        # Update the dictionary with the new data
        existing_data["status_code"] = page.status_code
        existing_data["list_items"] = [
            item.text.strip() for item in soup.find_all("li", class_="nav-item")
        ]
        existing_data["div_text"] = (
            soup.find("div", class_="row").text.strip()
            if soup.find("div", class_="row")
            else None
        )

        # Printing the status code
        print("Status Code:", existing_data["status_code"])

        # Printing list items
        print("List Items:")
        for item in existing_data["list_items"]:
            print(item)

        # Printing div text
        if existing_data["div_text"]:
            print("Div Text:", existing_data["div_text"])
        else:
            print("No div element with class 'row' found.")

        # Save updated data back to the JSON file
        with open(json_file_path, "w") as json_file:
            json.dump(existing_data, json_file)

        print("Data updated and saved to 'webscraper.json' successfully.")

    else:
        print("Failed to retrieve the page. Status Code:", page.status_code)

except requests.RequestException as e:
    print("An error occurred:", e)

except Exception as e:
    print("An unexpected error occurred:", e)
