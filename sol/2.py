# another exmaple of scraping elements from static web page

import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://books.toscrape.com/"


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_book_elements = soup.find_all(name="article",
                                  attrs={"class" : "product_pod"})

book_list = []

for book in all_book_elements:
    book_title = book.find("h3").text
    book_price = book.find("div",class_="product_price").find("p", {"class" : "price_color"}).text[1:]
    book_url = book.find("a").get("href")

    book_list.append({
        "title" : book_title,
        "book_price" : book_price,
        "book_url" : book_url
    })


sorted_by_price_asc = sorted(book_list, key=lambda x : x["book_price"])
pprint(sorted_by_price_asc)