import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import search_page_locators as loc


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open_page(self):
        with allure.step(f'Open Page {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)
            self.accept_cookies()

    def get_shadow_root(self, element):
        return self.driver.execute_script('return arguments[0].shadowRoot', element)

    def accept_cookies(self):
        try:
            shadow_host = self.driver.find_element(*loc.shadow_host_loc)
            shadow_root = self.get_shadow_root(shadow_host).find_element(*loc.accept_all_cookies_btn_loc)
            try:
                self.wait.until(EC.element_to_be_clickable(shadow_root))
                try:
                    shadow_root.click()
                except Exception as e:
                    print("Failed to accept cookies:", e)
            except TimeoutException:
                print("Accept all cookies button is not clickable")
        except Exception as e:
            print("Frame with cookies didn't appear:", e)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

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
        with allure.step('Scroll to chosen element on page '):
            self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def return_to_previous_page(self):
        return self.driver.back()

    def take_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG)

    def click_and_open_link_in_new_tab(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
        self.wait.until(EC.number_of_windows_to_be(2))

    def switch_to_new_tab(self, original_tab):
        all_tabs = self.driver.window_handles
        new_tab = next(tab for tab in all_tabs if tab != original_tab)
        self.driver.switch_to.window(new_tab)
