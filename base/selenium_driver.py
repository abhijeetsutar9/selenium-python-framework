from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import logging
import utilities.Custom_Logger as cl
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __int__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("Locator Type" + locatorType + "Not Supported")
        return False

    def getElement(self, driver, locator, locatorType="id"):
        element = None
        element = self.waitExplicitiely(driver, 10, locator, locatorType)
        return element

    def getElementList(self, driver, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator:: " + locator + "and locatorType:: " + locatorType)
        except:
            self.log.info("Element NOT list found with locator:: " + locator +
                          "and locatorType:: " + locatorType)
            return element

    def elementClick(self, logSource, driver, locator="", locatorType="id", element=None):
        try:
            if locator: #This means if locator is not empty
                element = self.getElement(driver, locator, locatorType)
            element.click()
            self.log.info(f"{logSource:} Clicked on element with locator: " + locator + " locatortype: " + locatorType)
        except:
            self.log.error("Cannot click on element with locator: " + locator +
                           " locatortype: " + locatorType)
            print_stack()

    def sendKeys(self, logSource, driver, data, locator="", locatorType="id", element=None):
        try:
            if locator: #This means if locator is not empty
                element = self.getElement(driver, locator, locatorType)
            element.send_keys(data)
            self.log.info(f"{logSource:} Sent data on element with locator: " + locator + " locatortype: " + locatorType)
        except:
            self.log.error(f"{logSource:} Cannot send data on element with locator: " + locator +
                           " locatortype: " + locatorType)
            print_stack()

    def getText(self, logSource, locator="", locatorType="id", element=None, info=""):
        try:
            if locator: #This means if locator is not empty
                self.log.debug(f"{logSource:} In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug(f"{logSource:} Before finding text")
            text = element.text
            self.log.debug(f"{logSource:} After find element, size is:: " + str(len(text)))
            if len(text) == 0:
                text= element.get_attribute(f"{logSource:} innerText")
            if len(text) != 0:
                self.log.info(f"{logSource:} Getting text on element:: " + info)
                self.log.info(f"{logSource:} The text of element is:: " + text + info)
                text = text.strip()
        except:
            self.log.error(f"{logSource:} Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    def isElementPresent(self, logSource, driver, locator="", locatorType="id", element=None):
        try:
            if locator: #This means if locator is not empty
                element = self.getElement(driver, locator, locatorType)
            if element is not None:
                self.log.info(f"{logSource:} Element Found with locator: " + locator + " locatortype: " + locatorType)
                return True
            else:
                self.log.error(f"{logSource:} Element Not Found with locator: " + locator + " locatortype: " + locatorType)
                return False
        except:
            self.log.error(f"{logSource:} Element Not Found with locator: " + locator + " locatortype: " + locatorType)
            return False

    def isElementDisplayed(self, logSource, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator: # This means if locatory is not empty
                element = self.getElement(locator, locatorType)
                self.log.info(f"{logSource:} Element is displayed with locator ::" + locator + " and locatorType ::" + locatorType)
            else:
                self.log.info(f"{logSource:} Element is NOT displayed with locator ::" + locator + " and locatorType ::" + locatorType)
            return isDisplayed
        except:
            self.log.info(f"{logSource:} Element is NOT displayed")
            return False


    def elementPresenceCheck(self, logSource, locator, locatorType):
        try:
            elementList = self.driver.find_elements(locatorType, locator)
            if len(elementList) > 0:
                self.log.info(f"{logSource:} Elements Found with locator: " + locator + " locatortype: " + locatorType)
                return True
            else:
                self.log.error(f"{logSource:} Element Not Found with locator: " + locator + " locatortype: " + locatorType)
                return False
        except:
            self.log.info(f"{logSource:} Elements No Found")
            return False

    def takeScreenshot(self, logSource, resultMessage):
        filName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + filName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f"{logSource:} Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error(f"{logSource:} ### Exception occured while taking screenshot")
            print_stack()


    def waitExplicitiely(self, driver, timeout, locator, locatorType="id"):
        element = None
        try:
            wait = WebDriverWait(driver, timeout=timeout, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((self.getByType(locatorType), locator)))
        except:
            self.log.error("Element not found")
        return element

    def scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 700);")

    def switchFrame(self, id="", name="", index=None):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDeafualtContent(self):
        self.driver.switch_to.default_content()
