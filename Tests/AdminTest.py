from Tests.PolyLearnBase import PolyLearnBase

class AdminTest(PolyLearnBase):

    def test_admin_login_as_user(self):
        # go to the list of users
        self.driver.get(self.url+"admin/user.php")
        self.driver.find_elements_by_css_selector("a[href*='/user/view']").pop(1).click()
        self.driver.find_elements_by_link_text('Log in as').pop().click()
        content_notice = self.driver.find_element_by_id('notice')
        self.assertTrue(expr=content_notice.text[:14] == 'You are logged',
                        msg="Unable to login as an admin")