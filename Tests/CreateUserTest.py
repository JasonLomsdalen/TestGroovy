from Tests.PolyLearnBase import PolyLearnBase
from Tests.User import User
from selenium.common.exceptions import NoSuchElementException
from SyntheticTestLauncher import TestRunner
import time

class CreateUserHelperMethods(PolyLearnBase):

    # Create new user given the specified fields in user
    def add_user(self, user):

        # go to the Site Administration -> Users -> Add a new user
        self.driver.get(self.url + "user/editadvanced.php?id=-1")

        # username
        self.driver.find_element_by_id('id_username').send_keys(user.username)

        # password
        self.driver.find_elements_by_link_text('Click to enter text').pop().click()
        self.driver.find_element_by_id('id_newpassword').send_keys(user.password)

        # first name
        self.driver.find_element_by_id('id_firstname').send_keys(user.firstname)

        # last name
        self.driver.find_element_by_id('id_lastname').send_keys(user.lastname)

        # email
        self.driver.find_element_by_id('id_email').send_keys(user.email)

        # ID number
        self.driver.find_element_by_xpath("//a[contains(@aria-controls,'id_moodle_optional')]").click()
        self.driver.find_element_by_id('id_idnumber').send_keys(user.idnumber)

        # EmplID
        self.driver.find_element_by_xpath("//a[contains(@aria-controls,'id_category_')]").click()
        self.driver.find_element_by_id('id_profile_field_emplid').clear()
        self.driver.find_element_by_id('id_profile_field_emplid').send_keys(user.emplid)

        # Add new user
        self.driver.find_element_by_id('id_submitbutton').click()
        time.sleep(2)
        # Test to see if fields were all filled out correctly and it added a user
        try:
            self.driver.find_element_by_id('page-admin-user')
        except NoSuchElementException:
            return False
        return True

    # Search for given user using their email
    def search_user(self, user):
        self.driver.get(self.url + "/admin/user.php")

        # reveal email filter text box
        self.driver.find_element_by_xpath("//a[contains(@class,'moreless-toggler')]").click()

        # enter email
        self.driver.find_element_by_id('id_email').send_keys(user.email)

        # add filter
        self.driver.find_element_by_id('id_addfilter').click()


    # Confirm the given user exists using their email
    def confirm_user(self, user):
        # Search for user
        CreateUserHelperMethods.search_user(self, user)

        # assertion that correct email appears
        try:
            self.driver.find_element_by_xpath("//td[contains(.,'" + user.email + "')]")
        except NoSuchElementException:
            self.driver.find_element_by_id('id_removeall').click()
            return False

        # clear filter
        self.driver.find_element_by_id('id_removeall').click()
        return True


    # Remove user from user list based off the given users email
    def remove_user(self, user):
        # Search for user
        CreateUserHelperMethods.search_user(self, user)

        # assertion that correct email appears
        try:
            self.driver.find_element_by_xpath("//td[contains(.,'" + user.email + "')]")
        except NoSuchElementException:
            self.driver.find_element_by_id('id_removeall').click()
            return False

        # press 'X' next to user to remove
        self.driver.find_element_by_xpath("//img[contains(@alt,'Delete')]").click()

        # confirm remove
        self.driver.find_element_by_xpath("//input[@value='Delete']").click()

        # clear filter
        self.driver.find_element_by_id('id_removeall').click()

        return True


class CreateUserTest(PolyLearnBase):

    # fake user account
    user_1 = User(TestRunner.config.values['username'], TestRunner.config.values['password'],
                  TestRunner.config.values['firstname'], TestRunner.config.values['lastname'],
                  TestRunner.config.values['altname'], TestRunner.config.values['email'])


    def test_a_add_user(self):
        self.assertTrue(expr=CreateUserHelperMethods.add_user(self, self.user_1),
                        msg="Adding user was not successful. Missing fields or user alredy exists.")

    def test_b_confirm_user(self):
        self.assertTrue(expr=CreateUserHelperMethods.confirm_user(self, self.user_1), msg="User doesn't exist")

    def test_c_remove_user(self):
        self.assertTrue(expr=CreateUserHelperMethods.remove_user(self, self.user_1), msg="Unable to remove given user")

