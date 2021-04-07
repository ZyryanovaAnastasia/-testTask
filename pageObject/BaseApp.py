import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import ActionChains


class BaseApp:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://mail.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


    def visibility_of_element_located(self, strategy, locator, message, timeout=10):
        WebDriverWait(self.wd, timeout).until(
            EC.visibility_of_element_located((strategy, locator)),
            F"За {timeout} сек:{message}"
        )
