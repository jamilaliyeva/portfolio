from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import saveCookies


class LoginPage:
    def __init__(self, driver):
        self.url = "https://veto-real.online/sign-in"
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 20)
        self.phone = (By.ID, "phone")
        self.login_button = (By.XPATH, "//button[@class='group font-medium justify-center whitespace-nowrap rounded-["
                                       "12px] disabled:pointer-events-none disabled:opacity-50 transition-all "
                                       "ease-in-out duration-200 w-full outline-none h-[52px] px-4 py-3.5 text-[16px] "
                                       "bg-primary-500 hover:bg-primary-600 focus:bg-primary-600 text-white "
                                       "disabled:bg-primary-100 disabled:text-primary-200 mb-7 flex items-center "
                                       "gap-2']")
        self.captcha_iframe = (By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        self.captcha_button = (By.ID, "recaptcha-anchor")
        self.otp_inputs = (By.XPATH, "//input[@inputmode='numeric']")
        self.confirm_button = (By.XPATH, "//button[contains(@class,'group font-medium justify-center whitespace-nowrap "
                                         "rounded-[12px] disabled:pointer-events-none disabled:opacity-50 "
                                         "transition-all ease-in-out duration-200 w-full outline-none h-[52px] px-4 "
                                         "py-3.5 text-[16px] bg-primary-500 hover:bg-primary-600 focus:bg-primary-600 "
                                         "text-white disabled:bg-primary-100 disabled:text-primary-200 mb-7 flex "
                                         "items-center gap-2')]")

    def load(self):
        self.driver.get(self.url)

    def set_username(self, phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    def click_captcha(self):
        # Switch to the reCAPTCHA iframe
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.captcha_iframe))

        # Wait until the captcha checkbox is clickable and then click it
        captcha = self.wait.until(EC.element_to_be_clickable(self.captcha_button))
        captcha.click()

        # Switch back to the main content
        self.driver.switch_to.default_content()

    def enter_otp(self, otp="000828"):
        # Wait for the OTP fields to be visible
        self.wait.until(EC.visibility_of_all_elements_located(self.otp_inputs))
        otp_elements = self.driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/main/form/div[1]/div/input")
        for i in range(len(otp_elements)):
            otp_elements[i].send_keys(otp[i])

    def click_login(self):
        # Option 1: Wait for the overlay to disappear (if you know what element it is)
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overlay-class")))

        # Option 2: Scroll the element into view
        login_button_element = self.driver.find_element(*self.login_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button_element)

        # Option 3: Click using JavaScript (if the above doesn't work)
        self.driver.execute_script("arguments[0].click();", login_button_element)

    def click_confirm(self):
        confirm_button_element = self.driver.find_element(*self.confirm_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button_element)
        self.driver.execute_script("arguments[0].click();", confirm_button_element)


def successful_login(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.set_username('709722389')
    login_page.click_login()
    login_page.click_captcha()
    login_page.enter_otp()
    login_page.click_confirm()
    saveCookies.saveCookies()

    login_page.wait.until(EC.url_contains("https://veto-real.online/"))

    assert "https://veto-real.online/" in driver.current_url
