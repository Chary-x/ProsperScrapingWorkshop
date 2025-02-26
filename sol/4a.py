from bs4 import BeautifulSoup
from pprint import pprint

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = "https://www.morganstanley.com/careers/career-opportunities-search?opportunity=sg"


service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)

seen_jobs = set()

def get_all_jobs_on_current_page():
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    job_elements = soup.find_all("div", class_="cmp-jobcard__content")

    for job in job_elements:
        job_title = job.find("div", class_="cmp-jobcard__title")
        job_link = job.find("a", class_="button--done")

        if job_title and job_link:
            title_text = job_title.get_text(strip=True)
            link_href = job_link['href']

            # create a unique key for each job
            job_key = (title_text, link_href)
            
            if job_key not in seen_jobs:
                seen_jobs.add(job_key)
                jobs.append({
                    "title": title_text,
                    "job_link": link_href
                })

def accept_cookies():
    accept_btn = driver.find_element(By.ID, "_evidon-accept-button")
    accept_btn.click()




jobs = []
driver.get(url)
accept_cookies()
while True:
    get_all_jobs_on_current_page()
    try:
        next_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".arrow.next")))
        next_btn.click()
    except Exception as e:
        print("No more pages to scrape.")
        break  

driver.quit()


pprint(jobs)
print(len(jobs))

# bs parses the entire page source at once, meaning previous pages’ 
# HTML might still be present in the source if the site loads content dynamically (e.g., AJAX pagination).