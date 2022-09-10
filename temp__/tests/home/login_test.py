from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from temp__.pages.home.login_page import Login_page
import unittest

class LoginTests(unittest.TestCase):
    def test_validLogin(self):
        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)
        driver.get(baseurl)

        lp = Login_page(driver)
        lp.login("test@email.com", "abcabc")

