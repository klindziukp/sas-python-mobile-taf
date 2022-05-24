import sys

from pageobject.main_page import MainPage
from pytest_testrail.plugin import pytestrail
import unittest
import pytest
import allure

sys.path.insert(0, '../..')


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class MainPageTestOther(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.main_page = MainPage(self.mobile_driver)

    @allure.story('other main page story')
    @allure.severity(allure.severity_level.NORMAL)
    @pytestrail.case('C3')
    def test_open_main_page_third(self):
        with allure.step('Navigate to main page other'):
            self.main_page.accept()
            self.main_page.play()
