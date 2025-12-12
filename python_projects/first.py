from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://matrixs.ai/sign-in")

wait = WebDriverWait(driver, 20)

email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))

email.send_keys("raish.momin@cognyx.ai")
password.send_keys("Test@123")

# FIX — choose the correct one:
driver.find_element(By.XPATH, "//button[@type='submit']").click()
