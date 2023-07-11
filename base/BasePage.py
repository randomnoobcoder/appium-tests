import unittest

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
import utilities.customlogger as cl
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = cl.customLogger()

    def waitForElement(self, locatorType, locatorValue):
        wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = None
        if locatorType == 'id':
            element = wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.ID, value=locatorValue)))
            return element
        elif locatorType == 'class':
            element = wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.CLASS_NAME, value=locatorValue)))
            return element
        elif locatorType == 'desc':
            element = wait.until(EC.visibility_of(
                self.driver.findElement(AppiumBy.ANDROID_UIAUTOMATOR,
                                        value=f'UiSelector.description("{locatorValue}")')))
            return element
        elif locatorType == "index":
            element = wait.until(EC.visibility_of(
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value=f'UiSelector().index({locatorValue})')))
            return element
        elif locatorType == "text":
            element = wait.until(EC.visibility_of(
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{locatorValue}")')))
            return element
        elif locatorType == "xpath":
            element = wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.XPATH, f'{locatorValue}')))
            return element
        else:
            self.log.info("Locator value " + locatorValue + "not found")
        return element

    def scrollIntoView(self, locatorValue):
        wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                 ElementNotSelectableException])
        wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                             f'UiScrollable(new UiSelector())'
                                                             f'.scrollIntoView(text("{locatorValue}"))')))

