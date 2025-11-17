from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

push_number = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
push_number.send_keys("Sky")

sleep(3)

push_number.clear()

sleep(2)

push_number.send_keys("Pro")

sleep(3)

driver.quit()

