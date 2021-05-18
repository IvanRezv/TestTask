from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_yandex_search():
    driver = WebDriver(executable_path="//Users//ivanrezv//PycharmProjects//Testwork//chromedriver")
    driver.get('https://yandex.ru')
    driver.find_element_by_xpath('//input[@id="text"]').send_keys("Тензор")

    # Проверка наличия таблицы с подсказками
    wait = WebDriverWait(driver, 2)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'popup_visible')]")))
    suggest = driver.find_element_by_xpath("//div[contains(@class,'popup_visible')]")
    print('\n', "Таблица с подсказками имеется - ", suggest.is_displayed())

    # Клик по кнопке поиска
    search_button = driver.find_element_by_xpath('//button[@type="submit"]').click()

    # Проверка наличия сайта
    sleep(2)
    links = driver.find_elements_by_css_selector('#search-result > .serp-item a.link > b')
    items = [elem.text.strip() for elem in links[:5]]
    if "tensor.ru" not in items:
        raise Exception('В первых пяти результатах нет сайта tensor.ru')
    else:
        print(" Сайт tensor.ru - присутствует в первых 5 элементах")

    driver.close()
    print("End of first task")