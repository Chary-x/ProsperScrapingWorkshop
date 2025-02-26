from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# local
FIREFOXDRIVER_PATH = "geckodriver.exe"
service1 = FirefoxService(executable_path=FIREFOXDRIVER_PATH)
# auto
service2 = FirefoxService(GeckoDriverManager().install())

driver = webdriver.Firefox(service=service2)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located(()))