import os
import time

from selenium import webdriver

try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля 
    input1 = browser.find_element_by_css_selector("input:nth-child(2)")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input:nth-child(4)")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input:nth-child(6)")
    input3.send_keys("mpers@yandex.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
