import pytest
import allure
from selenium import webdriver
from pages.CaclMainPage import CalcMainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка операций калькулятора с задержкой")
@allure.description("Тестирование основных арифметических операций с настраиваемой задержкой")
@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 45),
    ],
)
def test_calculator_flow(driver, num1, operation, num2, expected_result, delay):
    main_page = CalcMainPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        main_page.open()
    
    with allure.step(f"Установка задержки {delay} секунд"):
        main_page.set_delay(delay)
    
    with allure.step(f"Выполнение операции: {num1} {operation} {num2}"):
        main_page.click_buttons([num1, operation, num2, "="])
    
    with allure.step(f"Ожидание результата: {expected_result}"):
        main_page.wait_for_result(expected_result, delay)
    
    with allure.step("Проверка результата"):
        actual_result = main_page.get_result()
        assert actual_result == expected_result, \
            f"Ожидался результат: {expected_result}, получен: {actual_result}"