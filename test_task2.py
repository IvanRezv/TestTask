from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep


def test_yandex_pic():
    driver = WebDriver(executable_path="//Users//ivanrezv//PycharmProjects//Testwork//chromedriver")
    driver.get('https://yandex.ru')
    driver.find_element_by_xpath("//*[text()='Картинки']").click()
    driver.switch_to.window(driver.window_handles[1])

    # Проверка перехода в "Картинки"
    if driver.current_url != "https://yandex.ru/images/?utm_source=main_stripe_big":
        raise Exception("Перемещение на на тот сайт")
    else:
        print("\n", "Переход верный, ссылка корректная")

    # Обращение к первой категории
    driver.find_element_by_xpath(
        "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']").click()
    driver.implicitly_wait(5)
    images1 = driver.find_elements_by_class_name("serp-item__link")
    img_link = images1[0].get_attribute("href")

    # Открываем первую картинку
    driver.get(img_link)
    sleep(2)
    first_img_url = driver.current_url

    # Переходим ко второй
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
    sleep(2)

    # Переходим обратно к первой
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
    sleep(2)
    finally_check = driver.current_url

    # Проверка возврата на первую картинку
    if finally_check != first_img_url:
        raise Exception("Перемещение выполнено не на первую картинку")
    else:
        print("\n", "Все корректно, картинка верная")

    driver.close()
    driver.quit()
    print("End of second task")
