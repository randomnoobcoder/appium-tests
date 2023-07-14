import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from base.Driver import Driver
from base.BasePage import BasePage


@pytest.fixture(scope='class')
def setUpYoutube(request):
    print('\n \n ================== Starting YouTube Test session ==============')
    # appiumService = Driver()
    # appiumService.startAppiumService()
    driver = Driver.getDriver('com.google.android.youtube', 'com.google.android.apps.youtube.app.WatchWhileActivity')
    # driver.update_settings({"waitForIdleTimeout": 5})
    driver.implicitly_wait(3000)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print('\n Sleeping for 3 sec')
    time.sleep(3)
    driver.quit()
    # appiumService.stopAppiumService()
    print('\n ====================== Session End ===========================')


@pytest.fixture(scope='class')
def setUpFlipkart(request):
    print('\n \n ================== Starting Flipkart Test session ==============')
    # appiumService = Driver()
    # appiumService.startAppiumService()
    driver = Driver.getDriver('com.flipkart.android', 'com.flipkart.android.activity.HomeFragmentHolderActivity')
    driver.implicitly_wait(1000)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print('\n Sleeping for 3 sec')
    time.sleep(3)
    driver.quit()
    # appiumService.stopAppiumService()
    print('\n ====================== Session End ===========================')


@pytest.fixture(scope='class')
def initialSetupFlipkart(setUpFlipkart):
    print('------------- Setting up app to home screen ----------')
    driver = setUpFlipkart
    page = BasePage(driver)
    page.waitForElement("text", "English").click()
    page.waitForElement('id', 'com.flipkart.android:id/select_btn').click()
    page.waitForElement('id', 'com.google.android.gms:id/cancel').click()
    page.waitForElement('id', 'com.flipkart.android:id/custom_back_icon').click()
    driver.implicitly_wait(3000)
    print('------------------- At Home Screen Now ------------------')
