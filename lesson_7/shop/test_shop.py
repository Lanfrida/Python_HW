from selenium import webdriver
from login_page import LoginPage


def test_shop() -> None:
    # Инициализация драйвера
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    try:
        # Использование Page Object паттерна
        login_page = LoginPage(driver)
        
        # Цепочка вызовов методов (Fluent Interface)
        checkout_overview_page = (
            login_page
            .login("standard_user", "secret_sauce")
            .add_backpack_to_cart()
            .add_tshirt_to_cart()
            .add_onesie_to_cart()
            .go_to_cart()
            .proceed_to_checkout()
            .fill_shipping_info("Sofia", "Maslikova", "127247")
            .continue_to_overview()
        )
        
        # Получение итоговой суммы
        total_text = checkout_overview_page.get_total_amount()
        total_value = checkout_overview_page.extract_total_value()
        
        print(f"Итоговая стоимость: {total_text}")
        
        # Проверка
        expected_total = "$58.29"
        actual_total = f"${total_value}"
        
        assert actual_total == expected_total, (
            f"Ожидаемая сумма: {expected_total}, "
            f"Фактическая сумма: {actual_total}"
        )
        
        print(f"Проверка пройдена: итоговая сумма равна {expected_total}")
        
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_shop()