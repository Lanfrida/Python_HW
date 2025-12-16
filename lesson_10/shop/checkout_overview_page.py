from selenium.webdriver.common.by import By
from shop.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    # Локаторы
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    
    def get_total_text(self):
        """Возвращает полный текст, например 'Total: $58.29'"""
        total_element = self.find_element(*self.TOTAL_LABEL)
        return total_element.text
    
    def get_total_amount(self):
        """Возвращает только сумму, например '58.29'"""
        total_text = self.get_total_text()
        # Убираем "Total: " из текста
        amount = total_text.replace("Total: $", "")
        return amount
    
    def extract_total_value(self):
        """Алиас для get_total_amount() - возвращает только число"""
        return self.get_total_amount()