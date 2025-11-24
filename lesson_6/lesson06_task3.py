from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 40)
third_image = wait.until(EC.presence_of_element_located((By.ID, "award")))
src_attribute = third_image.get_attribute("src")
print(f"{src_attribute}")

driver.quit()


