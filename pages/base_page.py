from selenium.webdriver.chrome.webdriver import WebDriver
from pages.locators import base_page_locators as loc


class BasePage:
    base_url = 'https://swgoh.gg/'
    page_url = None
    list_of_available_filters = None
    filtered_chars_result = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        elif self.base_url:
            self.driver.get(f'{self.base_url}')
        else:
            raise NotImplementedError('Page cannot be opened by URL')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def scroll(self, pix=None):
        if not pix:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            self.driver.execute_script(f"window.scrollTo(0, {pix});")

    def click_filer_button(self):
        self.find(loc.filter_button_loc).click()

    def click_to_exact_filter(self, locator):
        self.find(locator).click()

    def check_filtered_characters_is_valid(self, filter_name):
        result_of_finding = self.find_all(loc.filtered_characters_loc)
        filtered_chars = list()
        for i in result_of_finding:
            filtered_chars.append(i.text)
        result_of_searching = len(filtered_chars)
        result_after_filtering = list(filter(lambda x: f'{filter_name}' in x, filtered_chars))
        ans = 1 if result_of_searching == len(result_after_filtering) else 0
        return ans
