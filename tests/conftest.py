import datetime

import pytest
from appium.webdriver.appium_service import AppiumService


from utilities import read_utils


@pytest.fixture(scope="session", autouse=True)
def start_appium_server():
    device=read_utils.get_value_from_json("../test_data/config.json","device")
    port=read_utils.get_value_from_json("../test_data/config.json","port")
    print(port,device)
    if device=="local":
        service = AppiumService()
        date = datetime.date.today()
        #service.start(args=['-a', 'localhost', '-p', '4723'])
        service.start(args=['-p', port, '-a', 'localhost', '--relaxed-security', '--base-path', '/wd/hub'])
        print(service.is_running)
        print(service.is_listening)
    yield
    if device == "local":
        service.stop()
