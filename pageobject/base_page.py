import logging
from time import sleep


from selenium.webdriver.common.by import By

LOGGER = logging.getLogger(__name__)


class BasePage:

    def __init__(self, mobile_driver):
        self.mobile_driver = mobile_driver

    def click_on_element(self, id_locator):
        LOGGER.info("Clicking on element with locator: %s", id_locator)
        element = self.mobile_driver.find_element(By.ID, id_locator)
        element.click()
        sleep(2)
