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
        self.wait = WebDriverWait(driver, 5, poll_frequency=1)

    def open_page(self):
        with allure.step(f'Open Page {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)
            self.accept_cookies()

    def accept_cookies(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(loc.cookies_frame_loc))

            try:
                # Wait for the "Accept All Cookies" button to appear and click it
                accept_cookies_button = self.wait.until(
                    EC.element_to_be_clickable(loc.accept_all_cookies_btn_loc))
                accept_cookies_button.click()
                # Switch back to the default content
                self.driver.switch_to.default_content()
            except Exception as e:
                print("Failed to accept cookies:", e)

        except TimeoutException:
            print("Frame with cookies did not appear.")

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

    def switch_to_new_tab(self, original_tab):
        all_tabs = self.driver.window_handles
        new_tab = next(tab for tab in all_tabs if tab != original_tab)
        self.driver.switch_to.window(new_tab)
