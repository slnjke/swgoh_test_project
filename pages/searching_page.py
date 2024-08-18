import allure
import logging
from base.base_page import BasePage
from config.links import Links
from pages.locators import search_page_locators as loc
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    PAGE_URL = Links.CHARACTERS_PAGE
    list_of_available_filters = None
    filtered_chars_result = None

    def click_filters_button(self):
        with allure.step("Click on filters button"):
            self.wait.until(EC.element_to_be_clickable(loc.filter_button_loc)).click()

    def click_on_a_specific_filter(self, locator):
        with allure.step(f"Select filter {locator[1].strip('//a[normalize-space(text()) =]')}"):
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def check_that_selected_filter_is_correct(self, locator):
        filter_to_select = locator[1].strip('//a[normalize-space(text()) =]')
        selected_filter = self.find(loc.selected_filter_loc).text

        return True if selected_filter in filter_to_select else False

    def check_filtered_characters_is_valid(self, locator):
        with allure.step(
                f"Checking that filtered characters is valid for filter "
                f"{locator[1].strip('//a[normalize-space(text()) =]')}"):

            selected_filter = self.find(loc.selected_filter_loc).text
            chars_filtered = self.find_all(loc.filtered_characters_loc)
            filtered_chars_names = self.find_all(loc.names_of_filtered_chars_loc)
            stats_of_filtered_chars = [element.text for element in chars_filtered]
            names_of_filtered_chars = [element.text for element in filtered_chars_names]
            dict_of_filters_chars = dict(zip(names_of_filtered_chars, stats_of_filtered_chars))
            self.take_screenshot("Character page")

            return True if all(selected_filter in val for val in dict_of_filters_chars.values()) else False

    def check_that_filtered_characters_is_valid(self, locator):
        with allure.step(
                f"Checking that filtered characters is valid for filter "
                f"{locator[1].strip('//a[normalize-space(text()) =]')}"):

            chars_filtered = self.find_all(loc.filtered_characters_loc)
            original_tab = self.driver.current_window_handle
            for char in chars_filtered:
                self.click_and_open_link_in_new_tab(char)
                self.switch_to_new_tab(original_tab)
                logging.debug("Checking presence of filter on character page")
                self.wait.until(EC.presence_of_element_located(locator))
                logging.debug("Closing page")
                self.driver.close()
                logging.debug("Switching to original tab")
                self.driver.switch_to.window(original_tab)

        return True
