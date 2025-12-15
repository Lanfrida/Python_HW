from selenium.webdriver.common.by import By
from base_page import BasePage
from cart_page import CartPage


class ProductsPage(BasePage):
    # Локаторы
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.CSS_SELECTOR, "a.shopping_cart_link")
    
    def add_backpack_to_cart(self):
        self.click_element(*self.ADD_BACKPACK_BUTTON)
        return self
    
    def add_tshirt_to_cart(self):
        self.click_element(*self.ADD_TSHIRT_BUTTON)
        return self
    
    def add_onesie_to_cart(self):
        self.click_element(*self.ADD_ONESIE_BUTTON)
        return self
    
    def go_to_cart(self):
        self.click_element(*self.CART_BUTTON)
        return CartPage(self.driver)