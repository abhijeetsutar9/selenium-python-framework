from selenium import webdriver
import time
import logging
import utilities.Custom_Logger as cl
from base.basePage import BasePage
from base.module_names import ModuleNames
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    m= ModuleNames()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[contains(text(),'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"
    _user_image = "//img[@src='/images/default-user-profile-pic.png']"
    _logout = "//div[@class='dropdown open']//a[@href='/logout']"
    _invalid_login = "//div[@class='form-group has-error']//span[contains(text(),'Your username or password is invalid. Please try again.')]"

    # Actions using selenium_driver
    def clickLoginLink(self):
        self.elementClick(logSource=self.m.Login_Module, driver=self.driver, locator=self._login_link,
                          locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(logSource=self.m.Login_Module, driver=self.driver, data= email, locator=self._email_field)

    def enterPassword(self, password):
        self.sendKeys(logSource=self.m.Login_Module, driver=self.driver, data= password,
                      locator=self._password_field)

    def clickLoginButton(self):
        self.elementClick(logSource=self.m.Login_Module, driver=self.driver, locator=self._login_button,
                          locatorType="xpath")

    # Test method using above defined actions and their methods
    def login(self, email, password):
        # time.sleep(3)
        self.clickLoginLink()
        # time.sleep(3)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyErrorSuccessful(self):
        result = self.isElementPresent(logSource=self.m.Login_Module, driver=self.driver,
                                       locator= "//div[contains(text(), 'Your email or password is incorrect.')]", locatorType="xpath")
        return result

    def goToHomepage(self):
        result = self.elementClick(logSource=self.m.Login_Module, driver=self.driver,
                                   locator= "//a[@class='navbar-brand header-logo']", locatorType="xpath")

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def verifySuccessfulLogin(self):
        result = self.isElementPresent(logSource=self.m.Login_Module, driver=self.driver,
                                       locator=self._user_image, locatorType="xpath")
        return result

    def userLogout(self):
        self.nav.navigateToUserImage()
        self.elementClick(logSource=self.m.Login_Module, driver=self.driver,
                          locator=self._logout, locatorType="xpath")

    def verifyLoginFailed(self):
        result = self.isElementPresent(logSource=self.m.Login_Module, driver=self.driver,
                                       locator=self._invalid_login, locatorType="xpath")
        return result
