from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
    
    def fill_field(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)