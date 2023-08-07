from pages.base_page import BasePage
from pages.locators import base_page_locators as loc


def test_filter_characters(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    base_page.click_to_exact_filter(loc.filter_loc_501)
    assert base_page.check_filtered_characters_is_valid(category_filter) == 1
