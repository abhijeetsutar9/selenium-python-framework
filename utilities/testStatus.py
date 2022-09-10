import logging
from traceback import print_stack
from base.selenium_driver import SeleniumDriver
import utilities.Custom_Logger as cl


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.resultList = []

    def setResult(self, logSource, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASSED")
                    self.log.info(f"{logSource:} ### VERIFICATION SUCCESSFULL:: " + resultMessage)
                else:
                    self.resultList.append("FAILED")
                    self.log.info(f"{logSource:} ### VERIFICATION FAILED:: " + resultMessage)
                    self.takeScreenshot(logSource, resultMessage)
            else:
                self.resultList.append("FAILED")
                self.log.error(f"{logSource:} ### VERIFICATION FAILED:: " + resultMessage)
                self.takeScreenshot(logSource, resultMessage)
        except:
            self.resultList.append("FAILED")
            self.log.error(f"{logSource:} ### EXCEPTION OCCURED!")
            self.takeScreenshot(logSource, resultMessage)
            print_stack()

    def mark(self, logSource, result, resultMessage):

        # Mark the result of verification point in a test case
        self.setResult(logSource, result, resultMessage)

    def markFinal(self, logSource, testName, result, resultMessage):

        # Mark the final result of the verification point in a testcase
        # This needs to be called at least once in a test case
        # This will be final test status of the test case
        self.setResult(logSource, result, resultMessage)

        if "FAILED" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST PASSED")
            self.resultList.clear()
            assert True == True


