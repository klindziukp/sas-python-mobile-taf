import pytest
import logging
from factory.mobile_driver_factory import MobileDriverFactory

LOGGER = logging.getLogger(__name__)


@pytest.fixture()
def set_up():
    LOGGER.info("Running method level set up")
    yield
    LOGGER.info("Running method level tear down")


@pytest.fixture(scope="class")
def one_time_set_up(request):
    """Mobile driver setup"""
    LOGGER.info("Running class set up")
    # TODO: Implement device selection from available device pool
    LOGGER.info("Selecting device from device pool")
    # TODO: Implement app installation to selected device
    LOGGER.info("Installing app to selected device")
    mobile_driver_factory = MobileDriverFactory()
    mobile_driver = mobile_driver_factory.get_mobile_driver_instance()

    if request.cls is not None:
        request.cls.mobile_driver = mobile_driver

    yield mobile_driver

    mobile_driver.quit()
    LOGGER.info("Running class tear down")


@pytest.fixture(scope='session', autouse=True)
def generate_allure_report():
    """Generate allure report"""
    LOGGER.info("Running suite set up")
    yield
    LOGGER.info("Running suite tear down")
