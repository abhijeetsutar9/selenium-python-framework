from selenium import webdriver
import time
import logging
import utilities.Custom_Logger as cl
from base.basePage import BasePage
from base.module_names import ModuleNames
from base.selenium_driver import SeleniumDriver

class RegisterForCourse(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    m = ModuleNames()

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # Locators
    _allCoursesLink = "//div[@id='navbar-inverse-collapse']//ul//li[2]//a"
    _allCoursesLabel = "//h1[contains(text(),'All Courses')]"
    _searchCourse = "//input[@id='search']"
    # _searchButton = "find-course search-course" #class
    _searchButton = "//button[@class='find-course search-course']//i[@class='fa fa-search']" #xpath
    _CourseLink = "//h4[contains(text(),'courseNameText')]"
    _submitEnroll = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _orderSummaryText = "//h4[contains(text(),'Order Summary')]"
    _ccNum = "//div[@class='CardNumberField-input-wrapper']//span//input"
    _ccExp = "exp-date" #name
    _ccCvv = "cvc" #name
    _clickBuyBtn = "//div[@class='col-xs-12']//i[@class='fa fa-arrow-right']" #to be re-visited
    _enrollErrorMsg = "//li[@class='card-no cvc expiry text-danger']//span"


    def clickAllCourses(self):

        self.elementClick(logSource=self.m.Course_Module, driver=self.driver, locator=self._allCoursesLink,
                              locatorType="xpath")

        result = self.isElementPresent(logSource=self.m.Course_Module, driver=self.driver, locator=self._allCoursesLabel,
                              locatorType="xpath")
        return result

    def searchCourses(self, courseName):
        self.sendKeys(logSource=self.m.Course_Module, driver=self.driver, data=courseName, locator=self._searchCourse,
                              locatorType="xpath")
        self.elementClick(logSource=self.m.Course_Module, driver=self.driver, locator=self._searchButton,
                              locatorType="xpath")

    # def clickSearchButton(self):
    #     result1 = self.elementClick(logSource=self.m.Course_Module, driver=self.driver, locator=self._searchButton,
    #                           locatorType="xpath")
    #     return result1

    def isCourseDisplayed(self):
        result = self.isElementPresent(logSource=self.m.Course_Module, driver=self.driver,
                                       locator=self._CourseLink, locatorType='xpath')
        return result

    def selectCourse(self, courseName):
        self._CourseLinkNew = self._CourseLink.replace('courseNameText', courseName)
        self.elementClick(logSource=self.m.Course_Module, driver=self.driver,
                                       locator=self._CourseLinkNew, locatorType='xpath')
        result = self.isElementPresent(logSource=self.m.Course_Module, driver=self.driver,
                                       locator=self._submitEnroll, locatorType='xpath')
        return result

    def clickEnrollCourse(self):
        self.elementClick(logSource=self.m.Course_Module, driver=self.driver,
                                       locator=self._submitEnroll, locatorType='xpath')
        result = self.isElementPresent(logSource=self.m.Course_Module, driver=self.driver,
                                       locator=self._orderSummaryText, locatorType='xpath')
        return result

    def buyCourse(self, ccNum, ccExp, ccCvv):
        self.switchFrame(index=1)
        self.sendKeys(logSource=self.m.Course_Module, driver=self.driver, data=ccNum, locator=self._ccNum,
                      locatorType="xpath")
        self.switchToDeafualtContent()

        self.switchFrame(index=2)
        self.sendKeys(logSource=self.m.Course_Module, driver=self.driver, data=ccExp, locator=self._ccExp,
                      locatorType="name")
        self.switchToDeafualtContent()

        self.switchFrame(index=3)
        self.sendKeys(logSource=self.m.Course_Module, driver=self.driver, data=ccCvv, locator=self._ccCvv,
                      locatorType="name")
        self.switchToDeafualtContent()

        self.elementClick(logSource=self.m.Course_Module, driver=self.driver,
                                       locator=self._clickBuyBtn, locatorType='xpath')

    def verifyFailedEnroll(self):
        result = self.isElementPresent(logSource=self.m.Course_Module, driver=self.driver,
                                       locator=self._enrollErrorMsg, locatorType='xpath')
        return result









