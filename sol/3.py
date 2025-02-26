# introduce dynamic scraping + scripts

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pprint

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium
import webdriver_manager

FIREFOXDRIVER_PATH = "geckodriver.exe"
service = webdriver.firefox.service.Service(executable_path=FIREFOXDRIVER_PATH)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)

url = "https://books.toscrape.com/"
book_list = []

print(pprint.__version__)
def scrape_books_on_page():
    """Scrapes book data from the given page using bs4"""
    soup = BeautifulSoup(driver.page_source, "html.parser")

    all_book_elements = soup.find_all(name="article", class_="product_pod")

    for book in all_book_elements:
        book_title = book.find("h3").find("a")["title"]  
        book_price = book.find("p", class_="price_color").text[1:]  
        book_url = book.find("h3").find("a")["href"] 

        book_dict = {
            "title": book_title,
            "book_price": book_price,
            "book_url": url + book_url,  # convert relative to absolute url
        }
        book_list.append(book_dict)
        pprint(book_dict)

# open the website with Selenium
driver.get(url)
while True:
    # scrape the books from the current page
    scrape_books_on_page()
    try:
        # wait and find the "next" button if it exists
        next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.next a")))
        next_btn.click()  # click the button to move to the next page

    except Exception as E:
        print(E)
        print("No more pages found. Scraping complete")
        break  # exit loop if "next" button is not found


print("Sorting in asc order by book price...")
sorted_by_price_asc = sorted(book_list, key=lambda x: x["book_price"])
pprint(sorted_by_price_asc)

driver.quit()
