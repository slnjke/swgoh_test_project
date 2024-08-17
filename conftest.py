import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.DEBUG)


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
