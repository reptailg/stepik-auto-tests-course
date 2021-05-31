import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)


try:
    # код выполнения задачи
    browser.find_element_by_css_selector("button.btn").click()
    browser.switch_to.window(browser.window_handles[1])

    browser.find_element_by_css_selector("#answer").send_keys(calc(browser.find_element_by_css_selector('#input_value').text))


    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    print(browser.switch_to.alert.text)
    browser.quit()

