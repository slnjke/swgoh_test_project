from selenium.webdriver.common.by import By


filter_button_loc = (By.XPATH, "//button[@class='btn btn-default']")
filter_list_loc = (By.XPATH, "//div[@class='modal-body p-a-0 categories']/div[@class='modal-body-scroller']"
                             "/div[@class='media-list media-list-users list-group']")
filtered_characters_loc = (By.XPATH, "//small[@class='pull-right']")
filter_loc_501 = (By.XPATH, "//strong[text()='501st']")
