from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop() -> None:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")   
    log = driver.find_element(By.ID, "user-name")
    log.send_keys("standard_user")

    passw = driver.find_element(By.ID, "password")
    passw.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()

    t_shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    t_shirt.click()

    onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    busket = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
    busket.click()

    check = driver.find_element(By.ID, "checkout")
    check.click()

    fn = driver.find_element(By.ID, "first-name")
    fn.send_keys("Sofia")

    ln = driver.find_element(By.ID, "last-name")
    ln.send_keys("Maslikova")

    pc = driver.find_element(By.ID, "postal-code")
    pc.send_keys("127247")

    cont_button = driver.find_element(By.ID, "continue")
    cont_button.click()

    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_value = total_text.replace("Total: $", "")
    print(f"Итоговая стоимость: {total_text}")

    expected_total = "$58.29"
    actual_total = f"${total_value}"
            
    assert actual_total == expected_total, f"Ожидаемая сумма: {expected_total}, Фактическая сумма: {actual_total}"
    print(f"Проверка пройдена: итоговая сумма равна {expected_total}")

    driver.quit()
    