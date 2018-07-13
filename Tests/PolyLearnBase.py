import unittest
from SyntheticTestLauncher import TestRunner, get_driver

class PolyLearnBase(unittest.TestCase):
    url = TestRunner.config.base_url
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver(TestRunner.config.driver,
                                TestRunner.config.headless)
        cls.adminLogin()

    def setUp(self):
        suite = TestRunner()
        args = suite.setup_arguments()
        suite.load_configs(args)

    @classmethod
    def adminLogin(self):
        self.driver.get(self.url + "login/index.php?authCAS=noCAS")
        field_username = self.driver.find_element_by_id('username')
        field_username.send_keys(TestRunner.config.username)
        field_password = self.driver.find_element_by_id('password')
        field_password.send_keys(TestRunner.config.password)
        button_submit = self.driver.find_element_by_id('loginbtn')
        button_submit.click()

        logininfo = self.driver.find_element_by_class_name('logininfo')
        content = logininfo.get_attribute('textContent')

        self.assertTrue(self,
                        expr=content.find("You are logged in") >= 0,
                        msg="Unable to log in as the admin user")

    @classmethod
    def logout(self):
        self.driver.get(self.url + "login/logout.php")
        button_continue = self.driver.find_elements_by_css_selector(
            "input[value='Continue']")
        button_continue[0].click()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.logout()
        cls.driver.quit()