import requests 
from bs4 import BeautifulSoup

"""
task 1 : interacting with static web page elements (wikipedia)

1. send a GET request to fetch the HTML content of Wikipedia's main page
2. parse the HTML content using BeautifulSoup
3. find all paragraph elements

take a look at soup_template if you're stuck!

"""

url = "https://en.wikipedia.org"

response = requests.get(url)
print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("p").text)
