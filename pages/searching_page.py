from pages.base_page import BasePage
from pages.locators import search_page_locators as loc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
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
        with allure.step(f"Выбираем фильтр {locator[1].strip('//strong[text()=]a[text()=')}"):
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

    def check_that_filtered_characters_is_valid(self, filter_name):
        with allure.step("Проверяем, что отфильтрованные персонажи валидны"):
            for i in range(len(filter_name)):
                with allure.step(f"Проверяем фильтр {filter_name[i]}"):
                    self.driver.find_element(By.XPATH, f"//strong[text()='{filter_name[i]}']").click()
                    filtered_chars = self.driver.find_elements(By.XPATH,
                                                               "//li[@class='media list-group-item p-0 character']")
                    original_tab = self.driver.current_window_handle
                    for n in range(len(filtered_chars)):
                        actions = ActionChains(self.driver)
                        self.driver.execute_script("arguments[0].scrollIntoView();", filtered_chars[n])
                        actions.key_down(Keys.CONTROL).click(filtered_chars[n])
                        actions.perform()
                        all_tabs = self.driver.window_handles
                        for w in all_tabs:
                            if w != original_tab:
                                self.driver.switch_to.window(w)
                                sleep(0.5)
                        self.driver.find_element(By.XPATH, f"//a[text()[contains(.,'{filter_name[i]}')]]")
                        self.driver.close()
                        self.driver.switch_to.window(original_tab)
