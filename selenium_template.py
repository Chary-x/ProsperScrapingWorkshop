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


# for firefox....F
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
wait = webdriver.wait(driver, 10)

element_im_waiting_for = wait.until(EC.presence_of_element_located(ENTER_LOCATOR_TUPLE))

# for other browsers, the syntax follows but for the respective manager and service.
# if you have a driver locally installed, you can reference it's path in FirefoxService(PATH_HERE)