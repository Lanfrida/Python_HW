from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

btn = "button.btn-primary"

button_push = driver.find_element(By.CSS_SELECTOR, btn)

#button_push.send_keys(Keys.RETURN) - одна из версий выполнения скрипта.

button_push.click() #второй вариант выполнения скрипта

sleep(5)