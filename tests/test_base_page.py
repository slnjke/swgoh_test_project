from pages.base_page import BasePage
from pages.locators import base_page_locators as loc


def test_filter_characters_501(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_501)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[0]) == 1


def test_filter_characters_attacker(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Attacker)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[1]) == 1


def test_filter_characters_bad_batch(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Bad_Batch)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[2]) == 1


def test_filter_characters_bounty_hunter(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(25)
    base_page.click_to_exact_filter(loc.filter_loc_Bounty_Hunter)
    driver.implicitly_wait(25)
    assert base_page.check_filtered_characters_is_valid(category_filter[3]) == 1


def test_filter_characters_clone_trooper(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Clone_Trooper)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[4]) == 1


def test_filter_characters_droid(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Droid)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[5]) == 1


def test_filter_characters_empire(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Empire)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[6]) == 1


def test_filter_characters_ewok(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Ewok)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[7]) == 1


def test_filter_characters_first_order(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_First_Order)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[8]) == 1


def test_filter_characters_fleet_commander(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Fleet_Commander)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[9]) == 1


def test_filter_characters_galactic_legend(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Galactic_Legend)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[10]) == 1


def test_filter_characters_galactic_republic(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Galactic_Republic)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[11]) == 1


def test_filter_characters_geonosian(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Geonosian)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[12]) == 1


def test_filter_characters_healer(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Healer)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[13]) == 1


def test_filter_characters_hutt_cartel(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Hutt_Cartel)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[14]) == 1


def test_filter_characters_imperial_remnant(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Imperial_Remnant)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[15]) == 1


def test_filter_characters_imperial_trooper(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Imperial_Trooper)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[16]) == 1


def test_filter_characters_inquisitorius(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Inquisitorius)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[17]) == 1


def test_filter_characters_jawa(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Jawa)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[18]) == 1


def test_filter_characters_jedi(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Jedi)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[19]) == 1


def test_filter_characters_leader(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Leader)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[20]) == 1


def test_filter_characters_mandalorian(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Mandalorian)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[21]) == 1


def test_filter_characters_nightsister(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Nightsister)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[22]) == 1


def test_filter_characters_old_republic(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Old_Republic)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[23]) == 1


def test_filter_characters_pheonix(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Phoenix)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[24]) == 1


def test_filter_characters_rebel(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Rebel)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[25]) == 1


def test_filter_characters_rebel_fighter(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Rebel_Fighter)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[26]) == 1


def test_filter_characters_resistance(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Resistance)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[27]) == 1


def test_filter_characters_rogue_one(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Rogue_One)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[28]) == 1


def test_filter_characters_scoundrel(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Scoundrel)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[29]) == 1


def test_filter_characters_separatist(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Separatist)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[30]) == 1


def test_filter_characters_sith(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Sith)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[31]) == 1


def test_filter_characters_sith_empire(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Sith_Empire)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[32]) == 1


def test_filter_characters_smuggler(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Smuggler)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[33]) == 1


def test_filter_characters_support(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Support)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[34]) == 1


def test_filter_characters_tank(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Tank)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[35]) == 1


def test_filter_characters_tusken(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Tusken)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[36]) == 1


def test_filter_characters_unaligned_force_user(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Unaligned_Force_User)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[37]) == 1


def test_filter_characters_wookie(driver, category_filter):
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.click_filer_button()
    driver.implicitly_wait(5)
    base_page.click_to_exact_filter(loc.filter_loc_Wookiee)
    driver.implicitly_wait(5)
    assert base_page.check_filtered_characters_is_valid(category_filter[38]) == 1
