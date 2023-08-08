from pages.searching_page import SearchPage
from pages.locators import search_page_locators as loc


class TestFilterCharactersByCategory:
    def test_filter_characters_501(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_501)
        assert search_page.check_filtered_characters_is_valid(category_filter[0]) == 1

    def test_filter_characters_attacker(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Attacker)
        assert search_page.check_filtered_characters_is_valid(category_filter[1]) == 1

    def test_filter_characters_bad_batch(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Bad_Batch)
        assert search_page.check_filtered_characters_is_valid(category_filter[2]) == 1

    def test_filter_characters_bounty_hunter(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        driver.implicitly_wait(25)
        search_page.click_on_a_specific_filter(loc.filter_loc_Bounty_Hunter)
        driver.implicitly_wait(25)
        assert search_page.check_filtered_characters_is_valid(category_filter[3]) == 1

    def test_filter_characters_clone_trooper(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Clone_Trooper)
        assert search_page.check_filtered_characters_is_valid(category_filter[4]) == 1

    def test_filter_characters_droid(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Droid)
        assert search_page.check_filtered_characters_is_valid(category_filter[5]) == 1

    def test_filter_characters_empire(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Empire)
        assert search_page.check_filtered_characters_is_valid(category_filter[6]) == 1

    def test_filter_characters_ewok(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Ewok)
        assert search_page.check_filtered_characters_is_valid(category_filter[7]) == 1

    def test_filter_characters_first_order(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_First_Order)
        assert search_page.check_filtered_characters_is_valid(category_filter[8]) == 1

    def test_filter_characters_fleet_commander(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Fleet_Commander)
        assert search_page.check_filtered_characters_is_valid(category_filter[9]) == 1

    def test_filter_characters_galactic_legend(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Galactic_Legend)
        assert search_page.check_filtered_characters_is_valid(category_filter[10]) == 1

    def test_filter_characters_galactic_republic(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Galactic_Republic)
        assert search_page.check_filtered_characters_is_valid(category_filter[11]) == 1

    def test_filter_characters_geonosian(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Geonosian)
        assert search_page.check_filtered_characters_is_valid(category_filter[12]) == 1

    def test_filter_characters_healer(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Healer)
        assert search_page.check_filtered_characters_is_valid(category_filter[13]) == 1

    def test_filter_characters_hutt_cartel(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Hutt_Cartel)
        assert search_page.check_filtered_characters_is_valid(category_filter[14]) == 1

    def test_filter_characters_imperial_remnant(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Imperial_Remnant)
        assert search_page.check_filtered_characters_is_valid(category_filter[15]) == 1

    def test_filter_characters_imperial_trooper(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Imperial_Trooper)
        assert search_page.check_filtered_characters_is_valid(category_filter[16]) == 1

    def test_filter_characters_inquisitorius(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Inquisitorius)
        assert search_page.check_filtered_characters_is_valid(category_filter[17]) == 1

    def test_filter_characters_jawa(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Jawa)
        assert search_page.check_filtered_characters_is_valid(category_filter[18]) == 1

    def test_filter_characters_jedi(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Jedi)
        assert search_page.check_filtered_characters_is_valid(category_filter[19]) == 1

    def test_filter_characters_leader(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Leader)
        assert search_page.check_filtered_characters_is_valid(category_filter[20]) == 1

    def test_filter_characters_mandalorian(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Mandalorian)
        assert search_page.check_filtered_characters_is_valid(category_filter[21]) == 1

    def test_filter_characters_nightsister(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Nightsister)
        assert search_page.check_filtered_characters_is_valid(category_filter[22]) == 1

    def test_filter_characters_old_republic(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Old_Republic)
        assert search_page.check_filtered_characters_is_valid(category_filter[23]) == 1

    def test_filter_characters_pheonix(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Phoenix)
        assert search_page.check_filtered_characters_is_valid(category_filter[24]) == 1

    def test_filter_characters_rebel(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Rebel)
        assert search_page.check_filtered_characters_is_valid(category_filter[25]) == 1

    def test_filter_characters_rebel_fighter(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Rebel_Fighter)
        assert search_page.check_filtered_characters_is_valid(category_filter[26]) == 1

    def test_filter_characters_resistance(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Resistance)
        assert search_page.check_filtered_characters_is_valid(category_filter[27]) == 1

    def test_filter_characters_rogue_one(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Rogue_One)
        assert search_page.check_filtered_characters_is_valid(category_filter[28]) == 1

    def test_filter_characters_scoundrel(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Scoundrel)
        assert search_page.check_filtered_characters_is_valid(category_filter[29]) == 1

    def test_filter_characters_separatist(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Separatist)
        assert search_page.check_filtered_characters_is_valid(category_filter[30]) == 1

    def test_filter_characters_sith(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Sith)
        assert search_page.check_filtered_characters_is_valid(category_filter[31]) == 1

    def test_filter_characters_sith_empire(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Sith_Empire)
        assert search_page.check_filtered_characters_is_valid(category_filter[32]) == 1

    def test_filter_characters_smuggler(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Smuggler)
        assert search_page.check_filtered_characters_is_valid(category_filter[33]) == 1

    def test_filter_characters_support(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Support)
        assert search_page.check_filtered_characters_is_valid(category_filter[34]) == 1

    def test_filter_characters_tank(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Tank)
        assert search_page.check_filtered_characters_is_valid(category_filter[35]) == 1

    def test_filter_characters_tusken(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Tusken)
        assert search_page.check_filtered_characters_is_valid(category_filter[36]) == 1

    def test_filter_characters_unaligned_force_user(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Unaligned_Force_User)
        assert search_page.check_filtered_characters_is_valid(category_filter[37]) == 1

    def test_filter_characters_wookie(self, driver, category_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.filter_loc_Wookiee)
        assert search_page.check_filtered_characters_is_valid(category_filter[38]) == 1


class TestFilterCharactersByAlignment:
    def test_filter_characters_light_side(self, driver, alignment_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.alignments_button_filter_loc)
        search_page.click_on_a_specific_filter(loc.filter_loc_Light_Side)
        assert search_page.check_filtered_characters_is_valid(alignment_filter[0]) == 1

    def test_filter_characters_dark_side(self, driver, alignment_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.alignments_button_filter_loc)
        search_page.click_on_a_specific_filter(loc.filter_loc_Dark_Side)
        assert search_page.check_filtered_characters_is_valid(alignment_filter[1]) == 1

    def test_filter_characters_neutral(self, driver, alignment_filter):
        search_page = SearchPage(driver)
        search_page.open_page()
        search_page.click_filters_button()
        search_page.click_on_a_specific_filter(loc.alignments_button_filter_loc)
        search_page.click_on_a_specific_filter(loc.filter_loc_Neutral)
        assert search_page.check_filtered_characters_is_valid(alignment_filter[2]) == 1
