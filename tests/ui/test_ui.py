import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# import time -використовується для затримки прогляду виконання тесту

@pytest.mark.ui
def test_check_incorrect_username():
    # створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    # відкриваємо сторінку http://github.com/login
    driver.get("http://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@stakeinemail.com")

    # знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sing in
    btn_elem = driver.find_element(By. NAME, "commit")

    # Емулюємо клік лівою кнопкою миши
    btn_elem.click()
    
    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"  # символ "·" комбінація Alt + 0183(NumLock)
    # time.sleep(3) -використовується для затримки прогляду виконання тесту

    # закриваємо браузер
    driver.close()