import pytest
from pages.searching_page import SearchPage


class BaseTest:
    search_page: SearchPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.search_page = SearchPage(driver)
