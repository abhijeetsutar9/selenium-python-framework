import unittest
from tests.home.loginTests import LoginTests
from tests.courses.registerCoursesCSVdata_test import RegisterCoursesCSVDataTests

# Get all tests from test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

# Run test suite
unittest.TextTestRunner(verbosity=2).run(smokeTest)