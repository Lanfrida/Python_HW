from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")
waiter = WebDriverWait(driver, 60)

button_name = "#newButtonName"
name_button = driver.find_element(By.CSS_SELECTOR, button_name)
name_button.send_keys("Skypro")


upd = "#updatingButton"
push_button = driver.find_element(By.CSS_SELECTOR, upd).click()

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(button.text)

driver.quit()