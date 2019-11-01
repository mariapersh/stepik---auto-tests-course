import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

try:
    x_element = browser.find_element_by_css_selector("#num1")
    y_element = browser.find_element_by_css_selector("#num2")
    x = x_element.text
    y = y_element.text
    sum_el = int(x) + int(y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum_el))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд 
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
