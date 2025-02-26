
"""
PROPER GRAMMAR, WE ARE GETTING SERIOUS NOW!!!

Task 4 : interacting with dynamic page elements (morgan stanley careers site)

Your task is to scrape all the jobs on this endpoint.


1. Scrape all jobs on this page
2. Format the jobs into a list of job dictionary objects
    List[Dict[str, str]] =  [
                                {
                                    "title" : {title_text},
                                    "link" : {link_href}
                                }
                            ]
3. Repeat until all jobs are scraped.
"""
import requests 
from bs4 import BeautifulSoup

from pprint import pprint

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService    
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://www.morganstanley.com/careers/career-opportunities-search?opportunity=sg"