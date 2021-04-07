import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome('/home/anastasia/repository/testEx/chromedriver')
    browser.maximize_window()
    yield browser
    browser.quit()
