from selenium import webdriver
import os

import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# import HtmlTestRunner


class VirtualCall(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.driver = webdriver.Firefox(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        # self.driver.maximize_window()
        # chrome_options = webdriver.ChromeOptions()
        #
        # chrome_options.add_argument('--headless')
        for x in range(1,11):
            self.driver = webdriver.Chrome('/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2')
            self.driver.maximize_window()

        # self.driver2 = webdriver.Chrome(executable_path="/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2")
        #
        # self.driver.maximize_window()
        # self.driver3 = webdriver.Chrome(executable_path="/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2")
        #
        # self.driver.maximize_window()
        # self.driver4 = webdriver.Chrome(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        #
        # self.driver4.maximize_window()
        #
        #
        # self.driver5 = webdriver.Chrome(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        #
        # self.driver5.maximize_window()
        #
        # self.driver6 = webdriver.Chrome(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        #
        # self.driver6.maximize_window()
        #
        # self.driver7 = webdriver.Chrome(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        #
        # self.driver7.maximize_window()
        #
        # self.driver8 = webdriver.Chrome(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        #
        # self.driver8.maximize_window()
        #
        # self.driver9 = webdriver.Chrome(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        #
        # self.driver9.maximize_window()
        #
        # self.driver10 = webdriver.Chrome(executable_path=("/Users/adeel/PycharmProjects/VideoCaliingTest/webdrivers/chromedriver 2"))
        #
        # self.driver10.maximize_window()


    # def test_first_attendee(self):
    #     self.driver.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver.implicitly_wait(25)
    #
    #
    #     email = self.driver.find_element_by_name(
    #         "email")
    #     email.send_keys("attendee1@gmail.com")
    #
    #     goToSession = self.driver.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_second_attendee(self):
    #     self.driver2.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver2.implicitly_wait(25)
    #     email = self.driver2.find_element_by_name(
    #         "email")
    #     email.send_keys("attendee2@gmail.com")
    #
    #     goToSession = self.driver2.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver2.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_third_attendee(self):
    #     self.driver3.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver3.implicitly_wait(25)
    #     email = self.driver3.find_element_by_name(
    #         "email")
    #     email.send_keys("attendee3@gmail.com")
    #
    #     goToSession = self.driver3.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver3.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_fourth_attendee(self):
    #     self.driver4.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver4.implicitly_wait(25)
    #     email = self.driver4.find_element_by_name(
    #         "email")
    #     email.send_keys("attendee4@gmail.com")
    #
    #     goToSession = self.driver4.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver4.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_fifth_attendee(self):
    #     self.driver5.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver5.implicitly_wait(25)
    #     email = self.driver5.find_element_by_name(
    #         "email")
    #     email.send_keys("attendee5@gmail.com")
    #
    #     goToSession = self.driver5.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver5.find_element_by_xpath(
    #         '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_sixth_attendee(self):
    #     self.driver6.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver6.implicitly_wait(25)
    #     email = self.driver6.find_element_by_name("email")
    #     email.send_keys("attendee6@gmail.com")
    #
    #     goToSession = self.driver6.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver6.find_element_by_xpath(
    #         '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_seventh_attendee(self):
    #     self.driver7.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver7.implicitly_wait(25)
    #     email = self.driver7.find_element_by_name("email")
    #     email.send_keys("attendee7@gmail.com")
    #
    #     goToSession = self.driver7.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver7.find_element_by_xpath(
    #         '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_eighth_attendee(self):
    #     self.driver8.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver8.implicitly_wait(25)
    #     email = self.driver8.find_element_by_name("email")
    #     email.send_keys("attendee8@gmail.com")
    #
    #     goToSession = self.driver8.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver8.find_element_by_xpath(
    #         '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()
    #
    # def test_ninth_attendee(self):
    #     self.driver9.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
    #     self.driver9.implicitly_wait(25)
    #     email = self.driver9.find_element_by_name("email")
    #     email.send_keys("attendee9@gmail.com")
    #
    #     goToSession = self.driver9.find_element_by_class_name("gCOXjb")
    #
    #     goToSession.click()
    #
    #     joinCall = self.driver9.find_element_by_xpath(
    #         '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')
    #
    #     joinCall.click()

    def test_tenth_attendee(self):
        for x in range(1,11):
            self.driver.get("https://dev-live.tame.events/event/990899b1-638a-4209-bf8f-f85662c5101c/sessions")
            self.driver.implicitly_wait(25)
            email = self.driver.find_element_by_name("email")
            email.send_keys(f"attendee{x}@gmail.com")

            goToSession = self.driver.find_element_by_class_name("gCOXjb")

            goToSession.click()

            joinCall = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/span[2]')

            joinCall.click()
    '''def test_Business_core_signin_firefox(self):
            email = self.driver2.find_element_by_xpath(
                "/html/body/div/div/main/div/div/div/div/div[3]/div/form/div[1]/div/div[1]/div/input")
            email.send_keys("admin@baernholdt.com")

            self.driver2.implicitly_wait(10)

            password1 = self.driver2.find_element_by_css_selector("[type='password']")

            password1.send_keys("secret")

            signin = self.driver2.find_element_by_xpath(
                "//*[@id='app']/div/main/div/div/div/div/div[3]/div/form/button/div")

            signin.click()'''

    '''def test_Business_core_signin_IE(self):
            email = self.driver3.find_element_by_xpath(
                "/html/body/div/div/main/div/div/div/div/div[3]/div/form/div[1]/div/div[1]/div/input")
            email.send_keys("admin@baernholdt.com")

            self.driver3.implicitly_wait(10)

            password1 = self.driver3.find_element_by_css_selector("[type='password']")

            password1.send_keys("secret")

            signin = self.driver3.find_element_by_xpath(
                "//*[@id='app']/div/main/div/div/div/div/div[3]/div/form/button/div")

            signin.click()'''

    @classmethod
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testMet1(self):
        pass


if __name__ == '__main__':
    unittest.main()