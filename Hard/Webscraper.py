import requests
from bs4 import BeautifulSoup

url = "https://shadowfox.in/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

print(page)
print(soup.prettify())  # Print the prettified HTML content
