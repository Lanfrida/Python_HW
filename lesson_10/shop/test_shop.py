import allure
from selenium import webdriver
from login_page import LoginPage


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест оформления заказа с проверкой итоговой суммы")
@allure.description("""
Тест проверяет полный процесс оформления заказа:
1. Авторизация
2. Добавление трех товаров в корзину
3. Переход в корзину
4. Оформление заказа
5. Проверка итоговой суммы
""")
def test_shop() -> None:
    # Инициализация драйвера
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    try:
        with allure.step("Открытие страницы авторизации"):
            login_page = LoginPage(driver)
        
        # Цепочка вызовов методов (Fluent Interface)
        with allure.step("Выполнение полного сценария оформления заказа"):
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
        with allure.step("Получение итоговой суммы заказа"):
            total_text = checkout_overview_page.get_total_amount()
            total_value = checkout_overview_page.extract_total_value()
            
            allure.attach(f"Итоговая стоимость: {total_text}", 
                         name="Итоговая сумма", 
                         attachment_type=allure.attachment_type.TEXT)
        
        # Проверка
        expected_total = "$58.29"
        actual_total = f"${total_value}"
        
        with allure.step(f"Проверка: ожидаемая сумма {expected_total}, фактическая {actual_total}"):
            assert actual_total == expected_total, (
                f"Ожидаемая сумма: {expected_total}, "
                f"Фактическая сумма: {actual_total}"
            )
            
        with allure.step("Тест пройден успешно"):
            print(f"Проверка пройдена: итоговая сумма равна {expected_total}")
        
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()


if __name__ == "__main__":
    test_shop()