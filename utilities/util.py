import time
import traceback
import random, string
import utilities.Custom_Logger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.INFO)

    def verifyTextContains(self, actualText, expectedText):
        self.log.info("Actual Text from Application Web UI-->:: " +actualText)
        self.log.info("Expected Text from Application Web UI-->::" + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS!")
            return True
        else:
            self.log.info("### VERIFICATION  DOES NOT CONTAINS!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        self.log.info("Actual Text from Application web UI:: " + actualText)
        self.log.info("Expected Text from Application web UI:: " + actualText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED")
            return True
        else:
            self.log.info("### VERIFICATION DID NOT MATCH!")
            return False
