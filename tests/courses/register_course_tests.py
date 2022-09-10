from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.courses.register_course import RegisterForCourse
import unittest
import pytest
import time
from utilities.testStatus import TestStatus
from base.module_names import ModuleNames

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class RegisterCourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.lp = RegisterForCourse(self.driver)
        self.ts = TestStatus(self.driver)
        self.m = ModuleNames()

    @pytest.mark.run(order=1)
    def test_allCourses(self):

        time.sleep(5)

        result1 = self.lp.clickAllCourses()
        # self.lp.searchCourses()
        self.ts.mark(logSource=self.m.Course_Module, result=result1, resultMessage="All courses home page opened")

    @pytest.mark.run(order=2)
    def test_searchCourses(self):
        self.lp.searchCourses()
        result = self.lp.isCourseDisplayed()
        self.ts.mark(logSource=self.m.Course_Module, result=result, resultMessage="Course displayed")


    @pytest.mark.run(order=3)
    def test_clickSearchButton(self):
        result = self.lp.selectCourse()
        self.ts.mark(logSource=self.m.Course_Module, result=result, resultMessage="Course selected successfully")

    @pytest.mark.run(order=4)
    def test_enrollForCourse(self):
        result = self.lp.clickEnrollCourse()
        self.lp.scroll("down")
        self.ts.mark(logSource=self.m.Course_Module, result=result, resultMessage="Clicked on Enroll Course button")

    @pytest.mark.run(order=5)
    def test_BuyCourseTest(self):
        self.lp.buyCourse(ccNum="5555555555554444", ccExp="1224", ccCvv="123")
        result = self.lp.verifyFailedEnroll()
        self.ts.mark(logSource=self.m.Course_Module, result=result, resultMessage="Error message displayed successfully")
        self.ts.markFinal(logSource=self.m.Course_Module, testName="test_BuyCourseTest",
                          result=result, resultMessage="Error message displayed successfully")







