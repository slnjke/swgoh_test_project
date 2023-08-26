from pages.base_page import BasePage
from pages.locators import search_page_locators as loc
import allure


class SearchPage(BasePage):
    base_url = 'https://swgoh.gg/'
    page_url = None
    list_of_available_filters = None
    filtered_chars_result = None

    def click_filters_button(self):
        with allure.step("Кликаем на кнопку выбора фильтров"):
            self.find(loc.filter_button_loc).click()

    def click_on_a_specific_filter(self, locator):
        with allure.step(f"Выбираем фильтр {locator}"):
            self.find(locator).click()

    def check_filtered_characters_is_valid(self, filter_name):
        with allure.step("Проверяем, что отфильтрованные персонажи валидны"):
            result_of_finding = self.find_all(loc.filtered_characters_loc)
            filtered_chars = list()
            for i in result_of_finding:
                filtered_chars.append(i.text)
            result_of_searching = len(filtered_chars)
            result_after_filtering = list(filter(lambda x: f'{filter_name}' in x, filtered_chars))
            ans = 1 if result_of_searching == len(result_after_filtering) else 0
            if ans == 0:
                raise AssertionError(f'One or more characters does not have tag: {filter_name}')
            else:
                return ans

    # def get_list_of_filtered_characters(self):
