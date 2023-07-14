from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
import utilities.customlogger as cl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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
            try:
                element = wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.ID, value=locatorValue)))
                self.log.info(f'Locator Found : {locatorValue}')
                return element
            except Exception as e:
                self.log.error(e)

        if locatorType == 'acc-id':
            try:
                element = wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value=locatorValue)))
                self.log.info(f'Locator Found : {locatorValue}')
                return element
            except Exception as e:
                self.log.error(e)

        elif locatorType == 'class':
            try:
                element = wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.CLASS_NAME, value=locatorValue)))
                self.log.info(f'Locator Found : {locatorValue}')
                return element
            except Exception as e:
                self.log.error(e)

        elif locatorType == 'desc':
            try:
                element = wait.until(EC.visibility_of(
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                            value=f'UiSelector().description("{locatorValue}")')))

                self.log.info(f'Locator Found : {locatorValue}')
                return element
            except Exception as e:
                self.log.error(e)

        elif locatorType == "index":
            try:
                element = wait.until(EC.visibility_of(
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value=f'UiSelector().index({locatorValue})')))
                self.log.info(f'Locator Found : {locatorValue}')
                return element
            except Exception as e:
                self.log.error(e)

        elif locatorType == "text":
            try:
                element = wait.until(EC.visibility_of(
                    self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{locatorValue}")')))
                self.log.info(f'Locator Found : {locatorValue}')
                return element
            except NoSuchElementException:
                self.log.error(f'Element {locatorValue} not found')

        elif locatorType == "xpath":
            try:
                element = wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.XPATH, f'{locatorValue}')))
                self.log.info(f'Locator Found : {locatorValue}')
                return element
            except Exception as e:
                self.log.error(e)

        else:
            self.log.info("Locator value " + locatorValue + "not found")
        return element

    def scrollIntoView(self, locatorValue):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of(self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 f'UiScrollable(new UiSelector())'
                                                                 f'.scrollIntoView(text("{locatorValue}"))')))
        except NoSuchElementException as e:
            print('Element not Found!!')
            self.log.error(f'ERROR : {e}')
