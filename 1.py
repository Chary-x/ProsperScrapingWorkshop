import requests 
from bs4 import BeautifulSoup
import bs4



"""
task 1 : interacting with static web page elements (wikipedia)

1. send a GET request to fetch the HTML content of Wikipedia's main page
2. parse the HTML content using BeautifulSoup
3. find all paragraph elements

"""

url = "https://en.wikipedia.org"

