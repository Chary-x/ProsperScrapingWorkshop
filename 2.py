import requests 
from bs4 import BeautifulSoup


"""
task 2 : interacting with static web page elements (book scraping site)

1. send a GET request to fetch the HTML content of the bookstoscrape main page
2. parse the HTML content using BeautifulSoup
3. find all book elements on the page
4. create a list of dictionary objects in the form  

[
    {
        "title" : book_title,
        "book_price" : book_price,
        "book_url" : book_url
    }
]

"""