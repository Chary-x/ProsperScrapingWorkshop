import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Main_Page")
soup = BeautifulSoup(response.text, 'html.parser')

first_paragraph = soup.find('p').text
print(first_paragraph)

