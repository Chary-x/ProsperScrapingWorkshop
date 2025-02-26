import requests 
from bs4 import BeautifulSoup


"""
task 3 : interacting with interactable page elements (book scraping site)

building from task2, we wish to add all books from the catalogue to our book list

STEPS 1-4 ARE THE SAME AS TASK 2

1. send a GET request to fetch the HTML content of the bookstoscrape main page
2. parse the HTML content using BeautifulSoup
3. find all book elements on the page
4. maintain a list of dictionary objects in the form  

[
    {
        "title" : book_title,
        "book_price" : book_price,
        "book_url" : book_url
    }
]


*** 

5. ensure that the list of dictionary objects contains EVERY book on the site 
        (locate the next button to propogate through the book list)

6. sort your list in ascending order of price
"""

url = "https://books.toscrape.com/"