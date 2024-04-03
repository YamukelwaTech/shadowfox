"""
Summary:
This Python script performs web scraping on the website "https://shadowfox.in/". It retrieves data from the website, including the HTTP status code, list items, and text from a specific div element. The script then updates an existing JSON file ('webscraper.json') with the retrieved data if the file exists, or creates a new JSON file if it doesn't. It handles various errors gracefully, including network-related errors and unexpected exceptions.

Libraries Used:
- requests: For sending HTTP requests to the website.
- BeautifulSoup (from bs4): For parsing HTML content.
- json: For handling JSON data.
- os: For interacting with the operating system, particularly for file path operations.

Variables:
- url: The URL of the website to scrape.
- json_file_path: The file path for the JSON file where scraped data will be stored.
- existing_data: A dictionary to store existing data from the JSON file or initialize an empty one.

Functions/Code Blocks:
1. Check if the JSON file exists and load existing data if available.
2. Send a GET request to the URL and check if the request was successful (status code 200).
3. Parse the HTML content of the page using BeautifulSoup.
4. Update the dictionary with new data, including status code, list items, and div text.
5. Print status code, list items, and div text.
6. Save updated data back to the JSON file.
7. Handle errors using try-except blocks, distinguishing between network-related errors and unexpected exceptions.

Execution:
The script initiates the web scraping process by sending a GET request to the specified URL. It then extracts relevant data from the HTML content and updates the JSON file accordingly. Error handling ensures that network issues or unexpected exceptions are properly managed, providing informative messages to the user.
"""


import requests
from bs4 import BeautifulSoup
import json
import os

# URL of the website to scrape
url = "https://shadowfox.in/"

# File path for the JSON file
json_file_path = "intermediate/webscraper.json"

# Check if the JSON file already exists
if os.path.exists(json_file_path):
    # If the JSON file exists, load existing data from it
    with open(json_file_path, "r") as json_file:
        existing_data = json.load(json_file)
else:
    # If the JSON file doesn't exist, initialize an empty dictionary
    existing_data = {}

try:
    # Sending a GET request to the URL
    page = requests.get(url)

    # Checking if the request was successful (status code 200)
    if page.status_code == 200:
        # Parsing the HTML content of the page
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
    # Handling network-related errors
    print("An error occurred:", e)

except Exception as e:
    # Handling unexpected errors
    print("An unexpected error occurred:", e)
