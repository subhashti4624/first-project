# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://matrixs.ai/")
# there is no need to use time.sleep(20)
time.sleep(20)

driver.find_element

# first step :- git add ./ ("first code")
# second step :- git commit -m 'you message'.git
# third step :- git push origin main/ pull



