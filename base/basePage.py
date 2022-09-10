# Base Page class implementation
# Methods implemented in this class are common to entire application and not a specific page in AUT
# This class needs to be inherited by all page classes
# This should not be used by creating object instances

from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get Title")
            print_stack()
            return False
