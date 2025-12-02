from selenium.webdriver.common.by import By
from base_page import BasePage
from product_page import ProductsPage


class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com")
    
    def login(self, username: str, password: str):
        self.fill_field(*self.USERNAME_INPUT, username)
        self.fill_field(*self.PASSWORD_INPUT, password)
        self.click_element(*self.LOGIN_BUTTON)
        return ProductsPage(self.driver)