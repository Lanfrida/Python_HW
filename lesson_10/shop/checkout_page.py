from selenium.webdriver.common.by import By
from shop.base_page import BasePage
from shop.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage(BasePage):
    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str):
        self.fill_field(*self.FIRST_NAME_INPUT, first_name)
        self.fill_field(*self.LAST_NAME_INPUT, last_name)
        self.fill_field(*self.POSTAL_CODE_INPUT, postal_code)
        return self
    
    def continue_to_overview(self):
        self.click_element(*self.CONTINUE_BUTTON)
        return CheckoutOverviewPage(self.driver)