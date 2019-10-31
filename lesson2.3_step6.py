from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try:  
	
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    window_before = browser.window_handles[0]

    time.sleep(3)
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
	
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
	
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


