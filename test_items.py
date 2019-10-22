from selenium.webdriver.common.by import By
import time


def test_basket_button_is_present(driver):
    driver.implicitly_wait(10)
    driver.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    #time.sleep(30)

    button = driver.find_element(By.ID, "add_to_basket_form")
    assert button.is_displayed() == True, "Button is not displayed"
