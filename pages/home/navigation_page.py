from selenium import webdriver
import time
import logging
import utilities.Custom_Logger as cl
from base.basePage import BasePage
from base.module_names import ModuleNames


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    m= ModuleNames()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "//div[@id='navbar-inverse-collapse']//li[4]//a[contains(text(),'MY COURSES')]"
    _all_courses = "//div[@id='navbar-inverse-collapse']//li[2]//a[contains(text(),'ALL COURSES')]"
    _support = "//div[@id='navbar-inverse-collapse']//li[3]//a[contains(text(),'SUPPORT')]"
    _user_image = "//img[@src='/images/default-user-profile-pic.png']"

    # Actions using selenium_driver
    def navigateToAllCourses(self):
        self.elementClick(logSource=self.m.Login_Module, driver=self.driver,
                          locator=self._all_courses, locatorType="xpath")
    def navigateToMyCourses(self):
        self.elementClick(logSource=self.m.Login_Module, driver=self.driver,
                          locator=self._my_courses, locatorType="xpath")

    def navigateToSupport(self):
        self.elementClick(logSource=self.m.Login_Module, driver=self.driver,
                          locator=self._support, locatorType="xpath")

    def navigateToUserImage(self):
        self.elementClick(logSource=self.m.Login_Module, driver=self.driver,
                          locator=self._user_image, locatorType="xpath")