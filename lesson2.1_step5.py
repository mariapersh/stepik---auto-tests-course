import math
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element_by_css_selector("[for='robotsRule']")
    robots_rule.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
