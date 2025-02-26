# A demo extracting elements on a static webpage

import requests
from bs4 import BeautifulSoup
from pprint import pprint


response = requests.get("https://en.wikipedia.org/wiki/Main_Page")
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")