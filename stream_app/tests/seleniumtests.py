from django.test import LiveServerTestCase
from selenium import webdriver

class StreamAppSeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX)
        super(StreamAppSeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(StreamAppSeleniumTests, cls).tearDownClass()
        cls.selenium.quit()

    def test_basic(self):
        self.selenium.get('http://google.com')
