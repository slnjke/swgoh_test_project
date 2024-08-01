import allure
from base.base_test import BaseTest
from pages.locators import search_page_locators as loc


@allure.feature('Filtering Characters')
@allure.story('Filtering by category')
class TestFilterCharactersByCategory(BaseTest):
    def test_filter_characters_501(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_501)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_501)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_501)

    def test_filter_characters_attacker(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Attacker)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Attacker)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Attacker)

    def test_filter_characters_bad_batch(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Bad_Batch)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Bad_Batch)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Bad_Batch)

    def test_filter_characters_bounty_hunter(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Bounty_Hunter)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Bounty_Hunter)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Bounty_Hunter)

    def test_filter_characters_clone_trooper(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Clone_Trooper)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Clone_Trooper)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Clone_Trooper)

    def test_filter_characters_droid(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Droid)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Droid)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Droid)

    def test_filter_characters_empire(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Empire)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Empire)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Empire)

    def test_filter_characters_ewok(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Ewok)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Ewok)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Ewok)

    def test_filter_characters_first_order(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_First_Order)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_First_Order)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_First_Order)

    def test_filter_characters_fleet_commander(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Fleet_Commander)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Fleet_Commander)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Fleet_Commander)

    def test_filter_characters_galactic_legend(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Galactic_Legend)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Galactic_Legend)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Galactic_Legend)

    def test_filter_characters_galactic_republic(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Galactic_Republic)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Galactic_Republic)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Galactic_Republic)

    def test_filter_characters_geonosian(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Geonosian)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Geonosian)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Geonosian)

    def test_filter_characters_gungan(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Gungan)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Gungan)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Gungan)

    def test_filter_characters_healer(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Healer)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Healer)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Healer)

    def test_filter_characters_hutt_cartel(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Hutt_Cartel)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Hutt_Cartel)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Hutt_Cartel)

    def test_filter_characters_imperial_remnant(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Imperial_Remnant)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Imperial_Remnant)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Imperial_Remnant)

    def test_filter_characters_imperial_trooper(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Imperial_Trooper)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Imperial_Trooper)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Imperial_Trooper)

    def test_filter_characters_inquisitorius(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Inquisitorius)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Inquisitorius)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Inquisitorius)

    def test_filter_characters_jawa(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Jawa)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Jawa)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Jawa)

    def test_filter_characters_jedi(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Jedi)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Jedi)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Jedi)

    def test_filter_characters_leader(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Leader)

    def test_filter_characters_mandalorian(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Mandalorian)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Mandalorian)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Mandalorian)

    def test_filter_characters_nightsister(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Nightsister)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Nightsister)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Nightsister)

    def test_filter_characters_old_republic(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Old_Republic)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Old_Republic)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Old_Republic)

    def test_filter_characters_pheonix(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Phoenix)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Phoenix)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Phoenix)

    def test_filter_characters_rebel(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Rebel)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Rebel)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Rebel)

    def test_filter_characters_rebel_fighter(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Rebel_Fighter)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Rebel_Fighter)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Rebel_Fighter)

    def test_filter_characters_resistance(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Resistance)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Resistance)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Resistance)

    def test_filter_characters_rogue_one(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Rogue_One)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Rogue_One)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Rogue_One)

    def test_filter_characters_scoundrel(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Scoundrel)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Scoundrel)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Scoundrel)

    def test_filter_characters_separatist(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Separatist)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Separatist)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Separatist)

    def test_filter_characters_sith(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Sith)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Sith)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Sith)

    def test_filter_characters_sith_empire(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Sith_Empire)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Sith_Empire)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Sith_Empire)

    def test_filter_characters_smuggler(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Smuggler)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Smuggler)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Smuggler)

    def test_filter_characters_support(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Support)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Support)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Support)

    def test_filter_characters_tank(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Tank)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Tank)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Tank)

    def test_filter_characters_tusken(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Tusken)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Tusken)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Tusken)

    def test_filter_characters_unaligned_force_user(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Unaligned_Force_User)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Unaligned_Force_User)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Unaligned_Force_User)

    def test_filter_characters_wookie(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Wookiee)
        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Wookiee)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Wookiee)


@allure.feature('Filtering Characters')
@allure.story('Filtering by alignment')
class TestFilterCharactersByAlignment(BaseTest):
    def test_filter_characters_light_side(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.alignments_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Light_Side)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Light_Side)

    def test_filter_characters_dark_side(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.alignments_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Dark_Side)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Dark_Side)

    def test_filter_characters_neutral(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.alignments_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Neutral)
        assert self.search_page.check_filtered_characters_is_valid(loc.filter_loc_Neutral)


@allure.feature('Filtering Characters')
@allure.story('Filtering by Ability Classes')
class TestFilterCharactersByAbilityClasses(BaseTest):
    def test_filter_characters_ability_block(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Ability_Block)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Ability_Block)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Ability_Block)

    def test_filter_characters_accuracy_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Accuracy_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Accuracy_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Accuracy_Down)

    def test_filter_characters_accuracy_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Accuracy_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Accuracy_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Accuracy_Up)

    def test_filter_characters_advantage(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Advantage)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Advantage)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Advantage)

    def test_filter_characters_anti_droid(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Anti_Droid)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Anti_Droid)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Anti_Droid)

    def test_filter_characters_aoe(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_AoE)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_AoE)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_AoE)

    def test_filter_characters_armor_shred(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Armor_Shred)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Armor_Shred)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Armor_Shred)

    def test_filter_characters_assist(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Assist)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Assist)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Assist)

    def test_filter_characters_blind(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Blind)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Blind)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Blind)

    def test_filter_characters_bonus_attack(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Bonus_Attack)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Bonus_Attack)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Bonus_Attack)

    def test_filter_characters_buff_immunity(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Buff_Immunity)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Buff_Immunity)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Buff_Immunity)

    def test_filter_characters_burning(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Burning)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Burning)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Burning)

    def test_filter_characters_counter(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Counter)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Counter)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Counter)

    def test_filter_characters_critical_chance_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Critical_Chance_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Critical_Chance_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Critical_Chance_Down)

    def test_filter_characters_critical_chance_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Critical_Chance_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Critical_Chance_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Critical_Chance_Up)

    def test_filter_characters_critical_damage_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Critical_Damage_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Critical_Damage_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Critical_Damage_Down)

    def test_filter_characters_critical_damage_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Critical_Damage_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Critical_Damage_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Critical_Damage_Up)

    def test_filter_characters_critical_hit_immunity(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Critical_Hit_Immunity)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Critical_Hit_Immunity)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Critical_Hit_Immunity)

    def test_filter_characters_damage_immunity(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Damage_Immunity)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Damage_Immunity)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Damage_Immunity)

    def test_filter_characters_daze(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Daze)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Daze)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Daze)

    def test_filter_characters_deathmark(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Deathmark)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Deathmark)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Deathmark)

    def test_filter_characters_defence_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Defence_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Defence_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Defence_Down)

    def test_filter_characters_defence_penetration_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Defence_Penetration_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Defence_Penetration_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Defence_Penetration_Up)

    def test_filter_characters_defence_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Defence_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Defence_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Defence_Up)

    def test_filter_characters_dispel(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Dispel)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Dispel)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Dispel)

    def test_filter_characters_dispel_all_allies(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Dispel_All_Allies)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Dispel_All_Allies)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Dispel_All_Allies)

    def test_filter_characters_dispel_all_enemies(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Dispel_All_Enemies)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Dispel_All_Enemies)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Dispel_All_Enemies)

    def test_filter_characters_dot(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_DoT)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_DoT)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_DoT)

    def test_filter_characters_doubt(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Doubt)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Doubt)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Doubt)

    def test_filter_characters_evasion_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Evasion_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Evasion_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Evasion_Down)

    def test_filter_characters_evasion_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Evasion_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Evasion_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Evasion_Up)

    def test_filter_characters_expose(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Expose)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Expose)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Expose)

    def test_filter_characters_fear(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Fear)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Fear)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Fear)

    def test_filter_characters_foresight(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Foresight)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Foresight)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Foresight)

    def test_filter_characters_frenzy(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Frenzy)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Frenzy)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Frenzy)

    def test_filter_characters_gain_turn_meter(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Gain_Turn_Meter)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Gain_Turn_Meter)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Gain_Turn_Meter)

    def test_filter_characters_heal(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Heal)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Heal)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Heal)

    def test_filter_characters_healing_immunity(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Healing_Immunity)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Healing_Immunity)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Healing_Immunity)

    def test_filter_characters_health_steal_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Health_Steal_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Health_Steal_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Health_Steal_Up)

    def test_filter_characters_health_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Health_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Health_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Health_Up)

    def test_filter_characters_inspired(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Inspired)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Inspired)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Inspired)

    def test_filter_characters_instant_defeat_immunity(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Instant_Defeat_Immunity)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Instant_Defeat_Immunity)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Instant_Defeat_Immunity)

    def test_filter_characters_leader_critical_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Critical_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Critical_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Critical_Up)

    def test_filter_characters_leader_defence_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Defense_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Defense_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Defense_Up)

    def test_filter_characters_leader_evasion_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Evasion_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Evasion_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Evasion_Up)

    def test_filter_characters_leader_max_health_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Max_Health_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Max_Health_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Max_Health_Up)

    def test_filter_characters_leader_speed_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Speed_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Speed_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Speed_Up)

    def test_filter_characters_leader_tenacity(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Tenacity_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Tenacity_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Tenacity_Up)

    def test_filter_characters_leader_assist(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Assist)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Assist)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Assist)

    def test_filter_characters_leader_foresight(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Foresight)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Foresight)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Foresight)

    def test_filter_characters_leader_healing(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Healing)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Healing)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Healing)

    def test_filter_characters_leader_health_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Health_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Health_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Health_Up)

    def test_filter_characters_leader_protection_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Leader_Protection_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Leader_Protection_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Leader_Protection_Up)

    def test_filter_characters_offence_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Offense_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Offense_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Offense_Down)

    def test_filter_characters_offence_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Offense_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Offense_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Offense_Up)

    def test_filter_characters_plague(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Plague)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Plague)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Plague)

    def test_filter_characters_potency_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Potency_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Potency_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Potency_Up)

    def test_filter_characters_provoked(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Provoked)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Provoked)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Provoked)

    def test_filter_characters_purge(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Purge)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Purge)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Purge)

    def test_filter_characters_reduce_cooldowns(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Reduce_Cooldowns)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Reduce_Cooldowns)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Reduce_Cooldowns)

    def test_filter_characters_remove_turn_meter(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Remove_Turn_Meter)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Remove_Turn_Meter)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Remove_Turn_Meter)

    def test_filter_characters_reset_cooldown(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Reset_Cooldown)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Reset_Cooldown)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Reset_Cooldown)

    def test_filter_characters_revive(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Revive)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Revive)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Revive)

    def test_filter_characters_riposte(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Riposte)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Riposte)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Riposte)

    def test_filter_characters_shock(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Shock)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Shock)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Shock)

    def test_filter_characters_speed_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Speed_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Speed_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Speed_Down)

    def test_filter_characters_speed_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Speed_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Speed_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Speed_Up)

    def test_filter_characters_stagger(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Stagger)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Stagger)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Stagger)

    def test_filter_characters_stealth(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Stealth)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Stealth)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Stealth)

    def test_filter_characters_stun(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Stun)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Stun)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Stun)

    def test_filter_characters_target_lock(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Target_Lock)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Target_Lock)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Target_Lock)

    def test_filter_characters_taunt(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Taunt)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Taunt)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Taunt)

    def test_filter_characters_tenacity_down(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Tenacity_Down)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Tenacity_Down)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Tenacity_Down)

    def test_filter_characters_tenacity_up(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Tenacity_Up)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Tenacity_Up)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Tenacity_Up)

    def test_filter_characters_thermal_detonator(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Thermal_Detonator)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Thermal_Detonator)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Thermal_Detonator)

    def test_filter_characters_torture(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Torture)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Torture)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Torture)

    def test_filter_characters_vulnerable(self):
        self.search_page.open_page()
        self.search_page.click_filters_button()
        self.search_page.click_on_a_specific_filter(loc.ability_button_filter_loc)
        self.search_page.click_on_a_specific_filter(loc.filter_loc_Vulnerable)

        assert self.search_page.check_that_selected_filter_is_correct(loc.filter_loc_Vulnerable)
        assert self.search_page.check_that_filtered_characters_is_valid(loc.filter_loc_Vulnerable)
