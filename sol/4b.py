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


def get_all_jobs_on_current_page():
    jobs_elements = driver.find_elements(By.CSS_SELECTOR, ".cmp-jobcard__content")
    for job in jobs_elements:
        job_title = job.find_element(By.CSS_SELECTOR, ".cmp-jobcard__title").text 
        if not job_title:
            continue
        job_link = job.find_element(By.CSS_SELECTOR, ".button--done").get_attribute("href")
        jobs.append({
            "title " : job_title,
            "job_link" : job_link
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

# selenium finds elements that are currently in the browser's active DOM. 
# it only interacts with elements at the time of execution, preventing duplicate storage.