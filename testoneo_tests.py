import email
import time
import unittest
import functional_helpers
from selenium import webdriver


class TestoneoTests(unittest.TestCase):

    # # Variables user_login function
    # loginButton = "//span[contains(text(),'Zaloguj się')]"
    # inputEmail = "//div[@class='col-md-6']//input[@name='email']"
    # inputPassword = "//input[@name='password']"
    # submitLoginButton = "//button[@id='submit-login']"

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/pl/'
        self.login_url = self.base_url + 'logowanie'
        self.hummingbird_url = "https://autodemo.testoneo.com/pl/men/1-1-hummingbird-printed-t-shirt.html"
        self.driver = webdriver.Chrome(executable_path=r'C:\Tests\chromedriver.exe')

    @classmethod
    def tearDown(self):
        self.driver.quit()

    # def user_login(self, driver, email, password):
    #     driver.find_element_by_xpath(self.loginButton).click()
    #     driver.find_element_by_xpath(self.inputEmail).send_keys(email)
    #     driver.find_element_by_xpath(self.inputPassword).send_keys(password)
    #     driver.find_element_by_xpath(self.submitLoginButton).click()

    def assert_element_text(self, driver, xpath, expected_text):
        element_text = driver.find_element_by_xpath(xpath).text
        self.assertEqual(expected_text, element_text,
                         f"Expected text is differ from expected for page url: {driver.current_url}")

    def test_login_text_header(self):
        expected_text = "Zaloguj się do swojego konta"
        xpath = "//header[@class='page-header']"
        driver = self.driver

        driver.get(self.login_url)
        self.assert_element_text(driver, xpath, expected_text)

    def test_correct_login(self):
        email = "markry@poczta.pl"
        password = "123456mk"
        driver = self.driver
        xpath = "//header[@class='page-header']"
        expected_text = "Twoje konto"

        driver.get(self.base_url)
        functional_helpers.user_login(driver, email, password)
        self.assert_element_text(driver, xpath, expected_text)

    def test_check_product_name(self):
        xpath = "//h1[@class='h1']"
        expected_text = "HUMMINGBIRD PRINTED T-SHIRT"
        driver = self.driver

        driver.get(self.hummingbird_url)
        self.assert_element_text(driver, xpath, expected_text)

    def test_check_product_price(self):
        xpath = "//span[@itemprop='price']"
        expected_text = "23,52 zł"
        driver = self.driver

        driver.get(self.hummingbird_url)
        self.assert_element_text(driver, xpath, expected_text)

    def test_incorrect_login(self):
        email = "murkrys@poczta.pk"
        password = "13245mlk"
        driver = self.driver
        xpath = "//li[@class='alert alert-danger']"
        expected_text = "Błąd uwierzytelniania."

        driver.get(self.base_url)
        functional_helpers.user_login(driver, email, password)
        self.assert_element_text(driver, xpath, expected_text)
