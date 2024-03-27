import requests
from bs4 import BeautifulSoup

url = "https://shadowfox.in/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

print(page.status_code)
# print(soup.prettify())
print(soup.find_all("li", class_="nav-item"))
print(soup.find("div", class_="row").text.strip())
