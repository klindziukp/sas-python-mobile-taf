import unittest
from test.test_main_page import MainPageTest
from test.test_main_page_other import MainPageTestOther

# Get all tests from the test classes
main_page_test = unittest.TestLoader().loadTestsFromTestCase(MainPageTest)
main_page_test_other = unittest.TestLoader().loadTestsFromTestCase(MainPageTestOther)

# Create a test suite combining all test classes
smoke_test = unittest.TestSuite([main_page_test, main_page_test_other])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
