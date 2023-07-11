from utilities import deviceinfo
from appium import webdriver
from appium.options.android import  UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


class Driver:
    def __init__(self):
        self.appiumService = AppiumService()

    # @staticmethod
    def startAppiumService(self):
        try:
            print("********************** Starting Appium Server *************************")
            self.appiumService.start()
            print("********************** Appium Server Running **************************")
        except Exception as e:
            print(f'Error while starting appium server :: {e}')

    def stopAppiumService(self):

        try:
            print("********************** Stopping Appium Server *************************")
            self.appiumService.stop()
        except Exception as e:
            print(f'Error while stopping appium server :: {e}')

    @staticmethod
    def getDriver(appPackage, appActivity):
        desired_caps = {'platformName': 'Android',
                        'automationName': 'UiAutomator2',
                        'platformVersion': deviceinfo.DeviceProperties.platformVersion(),
                        'deviceName': deviceinfo.DeviceProperties.deviceName(),
                        'appPackage': appPackage,
                        'appActivity': appActivity,
                        'autoGrantPermissions': 'true',
                        "ignoreHiddenApiPolicyError": "true"}
        print("\n")
        for key, value in desired_caps.items():
            print("{} : {}".format(key, value))
        print("\n")
        appium_server_url = 'http://localhost:4723'

        # Returns abs path relative to this file and not cwd
        # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps/Chess Free.apk'))
        driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
        return driver
