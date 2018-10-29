import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Tests\chromedriver.exe')

    def test_demo_login(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/logowanie_etap_1.html')
        title = driver.title
        print(f'Actual title: {title}')
        assert title == 'Eurobank - Bankowość Internetowa - Logowanie'

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/konta.html')
        title = driver.title
        print(f'Actual title: {title}')
        assert title == 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont'

    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/pulpit.html')
        title = driver.title
        print(f'Actual title: {title}')
        assert title == 'Eurobank - Bankowość Internetowa - Pulpit'

    def tearDown(self):
        self.driver.quit()


class MainTests2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Tests\chromedriver.exe')

    def test_demo_login(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(title)
        self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Logowanie',
                         f'Actual title differ from expected for page url: {url}')


    def test_demo_accounts(self):
        driver = self.driver
        web_address = 'http://demo.eurobank.pl/konta.html'
        driver.get(web_address)
        title = driver.title
        print(title)
        self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont',
                         f'Actual title differ from expected for page url: {url}')


    def test_demo_pulpit(self):
        driver = self.driver
        web_address = 'http://demo.eurobank.pl/pulpit.html'
        driver.get(web_address)
        title = driver.title
        print(title)
        self.assertEqual(title, 'Euroban - Bankowość Internetowa - Pulpit',
                         f'Actual title differ from expected for page url: {url}')


@classmethod
def tearDownClass(self):
    self.driver.quit()
