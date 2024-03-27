from bs4 import BeautifulSoup
import requests

# Send a GET request to the webpage
url = 'https://example.com'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the webpage
title = soup.title.string
print("Title of the webpage:", title)
