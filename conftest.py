from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


@pytest.fixture(scope='session')
def category_filter(driver):
    driver.get('https://swgoh.gg/')
    filter_button = driver.find_element(By.CSS_SELECTOR, "[data-target= '#filterModal']")
    filter_button.click()
    result = driver.find_elements(By.XPATH, "//div[@class='modal-body p-a-0 categories']"
                                            "/div[@class='modal-body-scroller']"
                                            "/div[@class='media-list media-list-users list-group']")
    list_of_available_filters = list()
    unused = [' Affiliation', ' Role', ' None', ' Species', ' Profession']
    excluded_filters = ['Cargo Ship Ship', 'Event Only', 'Capital Ship', '212th']
    for element in result:
        list_of_available_filters = element.text.split("\n")
        for char in unused:
            list_of_available_filters = list(map(lambda x: x.replace(f'{char}', ''), list_of_available_filters))
            list_of_available_filters = [x for x in list_of_available_filters if x not in excluded_filters]
        return list_of_available_filters


def pytest_generate_tests(metafunc):
    if "category_filter" in metafunc.fixturenames:
        metafunc.parametrize("category_filter", category_filter[0:])
