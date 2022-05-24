from pageobject.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, mobile_driver):
        super().__init__(mobile_driver)
        self.mobile_driver = mobile_driver

    def is_no_button_displayed(self):
        self.is_element_displayed("uk.co.aifactory.chessfree:id/NoButton")

    def accept(self):
        self.click_on_element("uk.co.aifactory.chessfree:id/YesButton")

    def play(self):
        self.click_on_element("uk.co.aifactory.chessfree:id/ButtonPlay")



