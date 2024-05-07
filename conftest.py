from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import search_page_locators as loc

import pytest


@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_window_size(2560, 1600)
    chrome_driver.implicitly_wait(6)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="session")
def accept_cookies(driver):
    driver.get('https://swgoh.gg/')
    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(loc.cookies_frame_loc))

        try:
            # Wait for the "Accept All Cookies" button to appear and click it
            accept_cookies_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(loc.accept_all_cookies_btn_loc))
            accept_cookies_button.click()
            # Switch back to the default content
            driver.switch_to.default_content()
        except Exception as e:
            print("Failed to accept cookies:", e)

    except TimeoutException:
        print("Frame with cookies did not appear.")
    yield


@pytest.fixture(scope='class')
def category_filter(driver, accept_cookies):
    driver.get('https://swgoh.gg/')
    filter_button = driver.find_element(By.CSS_SELECTOR, "[data-target= '#filterModal']")
    filter_button.click()
    result = driver.find_elements(By.XPATH, "//div[@class='modal-body p-a-0 categories']"
                                            "/div[@class='modal-body-scroller']"
                                            "/div[@class='media-list media-list-users list-group']")
    unused = [' Affiliation', ' Role', ' None', ' Species', ' Profession']
    excluded_filters = ['Cargo Ship Ship', 'Event Only', 'Capital Ship', '212th']
    for element in result:
        list_of_available_filters = element.text.split("\n")
        for char in unused:
            list_of_available_filters = list(map(lambda x: x.replace(f'{char}', ''), list_of_available_filters))
            list_of_available_filters = [x for x in list_of_available_filters if x not in excluded_filters]
        print(list_of_available_filters)
        return list_of_available_filters


@pytest.fixture(scope='class')
def alignment_filter(driver, accept_cookies):
    driver.get('https://swgoh.gg/')
    filter_button = driver.find_element(By.CSS_SELECTOR, "[data-target= '#filterModal']")
    filter_button.click()
    alignment_button = driver.find_element(By.XPATH, "//a[text()='Alignments']")
    alignment_button.click()
    result = driver.find_elements(By.XPATH, "//div[@class='modal-body p-a-0 alignments']"
                                            "/div[@class='modal-body-scroller']"
                                            "/div[@class='media-list media-list-users list-group']")
    for element in result:
        list_of_available_filters = element.text.split("\n")
        return list_of_available_filters


@pytest.fixture(scope='class')
def ability_classes_filter(driver, accept_cookies):
    list_of_available_filters = list()
    driver.get('https://swgoh.gg/')
    driver.find_element(By.CSS_SELECTOR, "[data-target= '#filterModal']").click()
    driver.find_element(By.XPATH, "//a[text()='Ability Classes']").click()
    result = driver.find_elements(By.XPATH, "//div[@class='modal-body p-a-0 abilities']"
                                            "/div[@class='modal-body-scroller']"
                                            "/div[@class='media-list media-list-users list-group']"
                                            "/a[@class='list-group-item']")
    for element in result:
        list_of_available_filters.append(element.text)
    return list_of_available_filters
