from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Login_page():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        loginLink = self.driver.find_element(By.LINK_TEXT,"Login")
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "email")
        emailField.send_keys("test@email.com")

        passwordField = self.driver.find_element(By.ID,"password")
        passwordField.send_keys("abcabc")

        time.sleep(3)

        loginButton = self.driver.find_element(By.NAME,"commit")
        loginButton.click()
