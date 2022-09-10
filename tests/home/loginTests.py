from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest
import time
from utilities.testStatus import TestStatus
from base.module_names import ModuleNames

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.m = ModuleNames()

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.verifySuccessfulLogin()
        result2=self.lp.verifySuccessfulLogin()
        self.ts.mark(logSource=self.m.Login_Module, result=result2, resultMessage="Login Successful")
        self.ts.markFinal(logSource=self.m.Login_Module, testName="test_validLogin",
                          result=result2, resultMessage="Login was successful")

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lp.userLogout()
        self.lp.login("abhijeetsutar@hotmail.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True








