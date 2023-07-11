import unittest

from appium import webdriver
from utilities.deviceinfo import DeviceProperties as dp


class Instagram(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': dp.platformVersion(),
                        'deviceName': dp.deviceName(),
                        'appPackage': 'com.instagram.android',
                        'appActivity': 'com.instagram.nux.activity.SignedOutFragmentActivity',
                        'autoGrantPermissions': 'true'}

        # Returns abs path relative to this file and not cwd
        # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps/Chess Free.apk'))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def test_01_remove(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Instagram)
    unittest.TextTestRunner(verbosity=2).run(suite)
