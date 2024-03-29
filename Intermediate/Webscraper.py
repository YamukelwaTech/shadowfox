import requests
from bs4 import BeautifulSoup
import json

url = "https://shadowfox.in/"

try:
    # Sending a GET request to the URL
    page = requests.get(url)

    # Checking if the request was successful
    if page.status_code == 200:
        # Parsing the HTML content
        soup = BeautifulSoup(page.text, "html.parser")

        # Create a dictionary to store the data
        data = {
            "status_code": page.status_code,
            "list_items": [
                item.text.strip() for item in soup.find_all("li", class_="nav-item")
            ],
            "div_text": (
                soup.find("div", class_="row").text.strip()
                if soup.find("div", class_="row")
                else None
            ),
        }

        # Printing the status code
        print("Status Code:", data["status_code"])

        # Printing list items
        print("List Items:")
        for item in data["list_items"]:
            print(item)

        # Printing div text
        if data["div_text"]:
            print("Div Text:", data["div_text"])
        else:
            print("No div element with class 'row' found.")

        # Save data to a JSON file
        with open("webscraper.json", "w") as json_file:
            json.dump(data, json_file)

        print("Data saved to 'webscraper.json' successfully.")

    else:
        print("Failed to retrieve the page. Status Code:", page.status_code)

except requests.RequestException as e:
    print("An error occurred:", e)

except Exception as e:
    print("An unexpected error occurred:", e)
