from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class BasePage:
    base_url = 'https://swgoh.gg/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        with allure.step('Открываем страницу'):
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

    def scroll_to_view(self, locator):
        with allure.step('Скроллим до нужного элемента на странице'):
            self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def return_to_previous_page(self):
        return self.driver.back()
