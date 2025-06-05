import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import loginPage
import saveCookies


class ValuationForm:
    def __init__(self, driver):
        self.url = "https://veto-real.online/"
        self.driver = driver
        self.driver.maximize_window()
        # self.driver.implicitly_wait(1)
        self.wait = WebDriverWait(driver, 10)
        self.selectMapAddress = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div['
                                           '2]/div[1]/div/div[3]/div/div/div/input')
        self.address_to_select = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div['
                                            '2]/div/div[2]/div[1]/div/div[3]/div/ul/li')
        self.valuation_button = (By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/button[2]")
        self.property_button = (By.XPATH, "/html/body/div[2]/main/div[1]/div/div[2]/div[2]")
        self.next_button = (By.XPATH, "/html/body/div[2]/main/div[1]/div/div[3]/button")
        self.online_button = (By.XPATH, "/html/body/div[2]/main/div[1]/div/div[2]/div")
        self.private_house = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]")
        self.form_next_button = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div/div[2]/button")
        self.user_name = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/input")
        self.user_surname = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/input")
        self.user_address = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[1]/div/input")
        self.map_select = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[2]/div/button")
        self.input_map_address = (By.XPATH,
                                  "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[2]/div["
                                  "1]/div/div[3]/div/div/div/input")
        self.map_confirm_button = (By.XPATH,
                                   "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[2]/div["
                                   "1]/div/div[3]/button")
        self.input_area = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[6]/div[2]/div/div[1]/div/input")
        self.next = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div/div[2]/button[2]")
        self.building_year = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div["
                                        "1]/div/input")
        self.building_maintenance_none = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]")
        self.building_maintenance = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]")
        self.building_maintenance_well = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]")
        self.building_maintenance_good = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]")
        self.building_maintenance_bad = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[3]")
        self.room_count = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[1]/div/div/input")
        self.floor_material_button = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[3]/div/button")
        self.floor_material_dropdown = (
            By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[3]/div/div/button[4]")

    # def click_add_n_times(self, n):
    #     count = self.driver.find_element_by_xpath(self.room_count_increase)
    #     for i in range(n):
    #         count.click()

    def load(self):
        self.driver.get(self.url)

    def choose_valuation_form(self):
        self.driver.find_element(*self.valuation_button).click()
        self.driver.find_element(*self.property_button).click()
        self.driver.find_element(*self.next_button).click()
        self.driver.find_element(*self.online_button).click()
        self.driver.find_element(*self.next_button).click()
        self.wait.until(EC.visibility_of_element_located(self.private_house)).click()
        self.wait.until(EC.visibility_of_element_located(self.form_next_button)).click()

    def insert_user_information(self, user_name, user_surname, user_address):
        time.sleep(1)
        self.driver.find_element(*self.user_name).send_keys(user_name)
        self.driver.find_element(*self.user_surname).send_keys(user_surname)
        self.driver.find_element(*self.user_address).send_keys(user_address)

    def add_location(self, map_address):
        time.sleep(1)
        self.driver.find_element(*self.map_select).click()
        self.wait.until(EC.visibility_of_element_located(self.input_map_address)).send_keys(map_address)
        self.wait.until(EC.visibility_of_element_located(self.selectMapAddress))
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.address_to_select)).click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.map_confirm_button)).click()

    def insert_area(self, input_area):
        time.sleep(1)
        address = self.driver.find_element(*self.input_area)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", address)
        address.send_keys(input_area)
        self.wait.until(EC.visibility_of_element_located(self.next)).click()

    def insert_building_information(self, building_year, room_count):
        time.sleep(2)
        self.driver.find_element(*self.building_year).send_keys(building_year)
        self.driver.find_element(*self.building_maintenance).click()
        self.wait.until(EC.visibility_of_element_located(self.building_maintenance_bad)).click()
        count = self.wait.until(EC.visibility_of_element_located(self.room_count))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", count)
        count.send_keys(room_count)
        self.driver.find_element(*self.floor_material_button).click()
        material = self.wait.until(EC.visibility_of_element_located(self.floor_material_dropdown))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", material)
        material.click()
        self.wait.until(EC.visibility_of_element_located(self.next)).click()
        time.sleep(5)


def successful_valuation():
    driver = webdriver.Chrome()
    loginPage.successful_login(driver)
    valuation = ValuationForm(driver)
    valuation.load()
    saveCookies.loadCookies()
    valuation.choose_valuation_form()
    valuation.insert_user_information("Jamila", "Aliyeva", "Pushkin street 12/14")
    valuation.add_location("Pushkin street 14")
    valuation.insert_area("72")
    valuation.insert_building_information("2012", "3")

    valuation.wait.until(EC.url_contains("https://veto-real.online/valuation/fye?step=technical-equipment"))

    assert "https://veto-real.online/valuation/fye?step=technical-equipment" in driver.current_url

    driver.quit()


successful_valuation()
