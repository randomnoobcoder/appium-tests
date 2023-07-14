# -------------Some Appium Notes ----------------------
# to kill running appium server : taskkill /F /IM node.exe

import multiprocessing as mp
import pytest
import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from base.BasePage import BasePage
from base.Driver import Driver

text_to_search = 'tujhme rab dikhta hai'
text_to_search_2 = 'rab ne bana di jodi'


@pytest.mark.usefixtures("setUpYoutube")
class YoutubeTestCases(unittest.TestCase):
    # driver = Driver.getDriver('com.google.android.youtube', 'com.google.android.apps.youtube.app.WatchWhileActivity')

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.page = BasePage(self.driver)

    # @pytest.mark.skip
    def test_01_is_app_installed(self):
        print("Checking if app is installed.......")
        assert self.driver.is_app_installed("com.google.android.youtube")

    # @pytest.mark.skip
    def test_02_app_version(self):
        # Click on Account icon
        self.page.waitForElement('desc', "Account").click()

        # #Click on Settings
        self.page.waitForElement('text', 'Settings').click()

        # Click on About
        self.page.scrollIntoView('About')
        self.page.waitForElement('text', 'About').click()

        # Check App Version
        ver = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.LinearLayout['
                                                             '6]/android.widget.RelativeLayout/android.widget'
                                                             '.TextView[2]')
        print("\n Value of version element :: {0}".format(ver.text))
        self.assertEqual(ver.text, "18.25.39")
        self.driver.close_app()

    # @pytest.mark.skip
    def test_03_changeAccount(self):
        self.driver.launch_app()
        user_to_log_in = 'Tuli Bandra'
        self.page.waitForElement('desc', "Account").click()
        self.page.waitForElement('id', 'com.google.android.youtube:id/account_name_container').click()
        # Check Logged In user
        logged_user = self.page.waitForElement('id', "com.google.android.youtube:id/email")
        print("\n Current Logged In User : {0} ".format(logged_user.text))
        if logged_user.get_attribute('text') == "samsone700@gmail.com":
            print('User already Logged in !')
            assert True
        else:
            account_list = []
            lst = self.driver.find_elements(AppiumBy.ID, value='com.google.android.youtube:id/name')
            for value in lst:
                ele_name = value.text
                account_list.append(ele_name)
            print(f'\n List of Accounts Added : {account_list}')
            if user_to_log_in in account_list:
                try:
                    self.page.waitForElement('text', user_to_log_in).click()
                    self.driver.implicitly_wait(5000)
                except Exception as e:
                    print("\n Element could not be located ", e)
        self.page.waitForElement('desc', "Account").click()
        current_user = self.page.waitForElement('id', 'com.google.android.youtube:id/account_name')
        self.assertEqual(current_user.text, user_to_log_in)
        self.driver.close_app()

    @pytest.mark.skip
    def test_04_videoPlayback(self):
        self.driver.launch_app()
        # Select Video
        print('\n ------------Running Video Playback test--------------- ')
        video = self.page.waitForElement('xpath', "//android.view.ViewGroup[@index='0']")
        print('\n Playing video {0}'.format(video.get_attribute('content-desc')))
        video.click()
        self.driver.implicitly_wait(10000)

        # Checking Video Playback
        TouchAction(self.driver).tap(x=361, y=217).perform()
        self.page.waitForElement('id', 'Pause video').click()
        # t1 = self.driver.find_element_by_xpath("//android.widget.TextView["
        #                                        "@resource-id='com.google.android.youtube:id/time_bar_current_time']").get_attribute(
        #     'text')
        t1 = self.page.waitForElement('id','com.google.android.youtube:id/time_bar_current_time').text
        t3 = t1.replace(':', '.')
        self.page.waitForElement('id','Play video').click()
        self.driver.implicitly_wait(5000)
        TouchAction(self.driver).tap(x=361, y=217).perform()
        self.page.waitForElement('id', 'Pause video').click()

        # t2 = self.driver.find_element_by_xpath("//android.widget.TextView["
        #                                        "@resource-id='com.google.android.youtube:id/time_bar_current_time']").get_attribute(
        #     'text')
        t2 = self.page.waitForElement('id','com.google.android.youtube:id/time_bar_current_time').text
        t4 = t2.replace(':', '.')
        if float(t4) > float(t3):
            print('\n Video is Playing')
            assert True
        else:
            print('\n Check Code--')
            assert False

    # @pytest.mark.skip
    def test_05_search(self):
        self.driver.launch_app()
        self.page.waitForElement('desc', 'Search').click()
        search_box = self.page.waitForElement('id', 'com.google.android.youtube:id/search_edit_text')
        search_box.send_keys(text_to_search)
        self.driver.press_keycode(66)  # Enter
        self.driver.implicitly_wait(5000)
        # self.page.waitForElement('id', 'com.google.android.youtube:id/results')
        result_list = []
        lst = self.driver.find_elements(AppiumBy.XPATH, value="//android.view.ViewGroup")
        for value in lst:
            ele_name = value.get_attribute('content-desc')
            if ele_name is not None:
                result_list.append(ele_name)
        print('\n Search Result :: {0} '.format(result_list))
        self.driver.implicitly_wait(5000)
        self.assertTrue(any(text_to_search in result.lower() or text_to_search_2 in result.lower() for result in result_list), msg='Value Not Matched')

    @pytest.mark.skip
    def test_06_multiAction(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(523, 1729)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(3)
        actions.w3c_actions.pointer_action.move_to_location(514, 342)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    # def tearDown(self):
    #     """Tear down the test"""
    #     self.driver.quit()
    #     print("**********************Stopping Appium Server****************************")
    #     self.appiumService.stop()

# if __name__ == '__main__':
#     test_youtube = YoutubeTestCases
#     suite = unittest.TestLoader().loadTestsFromTestCase(YoutubeTestCases)
#     unittest.TextTestRunner(verbosity=10).run(suite)
#     # device_list = deviceinfo.DeviceProperties.deviceSerial()
#     # pool = mp.Pool(processes=1)
#     # pool.map(unittest.TextTestRunner(verbosity=10).run(suite), device_list)
#     # pool.close()
#     # pool.join()
#     # pool.terminate()
