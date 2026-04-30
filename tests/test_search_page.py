import allure
import pytest
from base.base_test import BaseTest
from pages.locators import search_page_locators as loc


@allure.parent_suite('Filtering Characters')
@allure.suite('Filtering by category')

class TestFilterCharactersByCategory(BaseTest):
    @pytest.mark.parametrize("case", loc.filter_fraction_locators)
    def test_filter_characters_by_fraction(self, case):
        filter_name, filter_locator = case
        print(filter_locator)
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(filter_locator)
        assert self.search_page.check_that_selected_filter_is_correct(filter_locator)
        assert self.search_page.check_filtered_characters_is_valid(filter_locator)

    @pytest.mark.parametrize("case", loc.filter_abilities_locators)
    def test_filter_characters_by_abilities(self, case):
        filter_name, filter_locator = case
        print(filter_locator)
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(filter_locator)
        assert self.search_page.check_that_selected_filter_is_correct(filter_locator)
        assert self.search_page.check_filtered_characters_is_valid(filter_locator)
