from selenium.webdriver.common.by import By
from pages.courses.register_course import RegisterForCourse
from utilities.readData import getCSVData
from utilities.testStatus import TestStatus
from ddt import ddt, data, unpack
import unittest, pytest
import time
from base.module_names import ModuleNames
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetup):
        self.courses = RegisterForCourse(self.driver)
        self.ts = TestStatus(self.driver)
        self.mn = ModuleNames()
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\Dell\\workspace_python\\framworkdemo1\\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.searchCourses(courseName)
        self.courses.selectCourse(courseName)
        self.courses.clickEnrollCourse()
        self.courses.buyCourse(ccNum=ccNum, ccExp=ccExp, ccCvv=ccCVV)
        result = self.courses.verifyFailedEnroll()
        self.ts.markFinal(logSource=self.mn.Course_Module, testName="test_invalidEnrollment",
                          result=result, resultMessage="Enrollment Failed verification")



