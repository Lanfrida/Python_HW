from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_form() -> None:
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    filling_fn = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    filling_fn.send_keys("Иван")

    filling_ln = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    filling_ln.send_keys("Петров")

    ad_filling = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    ad_filling.send_keys("Ленина, 55-3")

    fm = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    fm.send_keys("test@skypro.com")

    fp = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    fp.send_keys("+7985899998787")

    fzc = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    fzc.send_keys("")

    fc = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    fc.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.send_keys("Россия")

    job = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    job.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.send_keys("Skypro")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    zip_code_field = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    zip_code_class = zip_code_field.get_attribute("class")
    if "danger" in zip_code_class:
        print("✓ Поле zip-code правильно подсвечено как обязательное")
    else:
        print("✗ Ошибка: поле zip-code не подсвечено как обязательное")
    assert "danger" in zip_code_class, "поле zip-code не подсвечивается как обязательное"

    driver.quit()
    