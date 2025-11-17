from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

btn = "button.btn-primary"

button_push = driver.find_element(By.CSS_SELECTOR, btn)
button_push.click()

sleep(5)

