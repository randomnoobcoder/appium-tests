import time
import unittest


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class SettingTestCases(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '9', 'deviceName': 'G$_MI6',
                        'appPackage': 'com.androidauthority.app',
                        'appActivity': 'com.androidauthority.app.ui.activity.mainscreen.MainScreenActivity',
                        'autoGrantPermissions': 'true'}

        # Returns abs path relative to this file and not cwd
        # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps/Chess Free.apk'))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def test_01_app_version(self):
        touch = TouchAction(self.driver)
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout["
            "2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
            ".FrameLayout/android.widget.ListView/android.widget.LinearLayout["
            "6]/android.widget.RelativeLayout/android.widget.TextView")
        while el3.text != 'Additional settings':
            touch.press(x=525, y=841).move_to(x=528, y=756).release().perform()
            time.sleep(1)
        el3.click()

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SettingTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)