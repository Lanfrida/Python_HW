from selenium.webdriver.common.by import By
from base_page import BasePage
from checkout_page import CheckoutPage


class CartPage(BasePage):
    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    def proceed_to_checkout(self):
        self.click_element(*self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)