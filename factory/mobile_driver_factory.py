"""
@package base
WebDriver Factory class implementation
It creates a web-driver instance based on browser configurations
"""
from selenium import webdriver
from appium import webdriver
from config.config_reader import get_app_config_param
from config.config_reader import get_device_config_param


class MobileDriverFactory:

    def __init__(self):
        """
        Inits WebDriverFactory class
        :Returns None:
        """

    def get_mobile_driver_instance(self):
        """
        Get MobileDriver Instance
        :return 'MobileDriver Instance':
        """

        desired_caps = {'platformName': get_device_config_param("platformName"),
                        'platformVersion': get_device_config_param("platformVersion"),
                        'deviceName': get_device_config_param("deviceName"),
                        'app': get_app_config_param("app"),
                        'appPackage': get_app_config_param("appPackage"),
                        'appActivity': get_app_config_param("appActivity")}
        mobile_driver = webdriver.Remote(get_device_config_param("driverUrl"), desired_caps)

        return mobile_driver
