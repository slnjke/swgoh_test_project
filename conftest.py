from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import search_page_locators as loc
import pytest


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1440, 900)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
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
