from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

un = "input[name='username']"
push_login = driver.find_element(By.CSS_SELECTOR, un)
push_login.send_keys("tomsmith")

sleep(1)

pw = "input[id='password']"
push_pass = driver.find_element(By.CSS_SELECTOR, pw)
push_pass.send_keys("SuperSecretPassword!")

sleep(2)

log = "button.radius"
push_log = driver.find_element(By.CSS_SELECTOR, log)
push_log.click()

success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text)

sleep(6)

driver.quit()


