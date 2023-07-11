# -------------Some Appium Notes ----------------------
# to kill running appium server : taskkill /F /IM node.exe

import multiprocessing as mp
import pytest
import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
import utilities.customlogger as cl

text = 'tujhme rab dikhta hai'

logger = cl.customLogger()


# Create obj of Driver class
# driver1 = Driver()

# Driver.startAppiumService()
#
# driver = Driver.getDriver()
@pytest.mark.usefixtures("setUpYoutube")
class YoutubeTestCases(unittest.TestCase):

    @pytest.mark.skip
    def test_05_multiAction(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(523, 1729)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(3)
        actions.w3c_actions.pointer_action.move_to_location(514, 342)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    # @pytest.mark.skip
    def test_is_app_installed(self) -> None:
        print("\n Checking if app is installed.......")
        assert self.driver.is_app_installed("com.google.android.youtube")

    # @pytest.mark.skip
    def test_01_app_version(self):
        # time.sleep(2)
        # WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(By.ID, ))
        # Click on Account icon
        self.driver.find_element(AppiumBy.ID, value="com.google.android.youtube:id/image").click()
        # time.sleep(2)
        # try:
        # #Click on Settings
        self.driver.find_element(AppiumBy.XPATH, value="//*[@text='Settings']").click()
        # except Exception as e:
        #     print('in except block')
        #     touch_action = TouchAction(self.driver)
        #     touch_action.long_press(x=453, y=1214).move_to(x=411, y=976).release().perform()
        #     time.sleep(2)
        #     self.driver.find_element_by_xpath("//*[@text='Settings']").click()

        # time.sleep(2)
        # Click on About
        try:
            self.driver.find_element(AppiumBy.XPATH, value="//*[@text='About']").click()
        except Exception as e:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(523, 1729)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(3)
            actions.w3c_actions.pointer_action.move_to_location(514, 342)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            # touch_action = TouchAction(self.driver)
            # touch_action.long_press(x=492, y=1331).move_to(x=488, y=1013).release().perform()
            # self.driver.find_element(AppiumBy.XPATH, value="//*[@text='About']").click()
        # time.sleep(2)
        # Check App Version
        ver = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.LinearLayout['
                                                             '6]/android.widget.RelativeLayout/android.widget'
                                                             '.TextView[2]')
        print("Value of version element :: {0}".format(ver.text))
        # ele = WebDriverWait.until()
        # try:
        self.assertEqual(ver.text, "15.14.33")

        # except Exception as e:
        #     print(e)

    @pytest.mark.skip
    def test_02_changeAccount(self):
        self.driver.find_element_by_accessibility_id("Account").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.google.android.youtube:id/account_name').click()
        time.sleep(1)
        # Check Logged In user
        logged_user = self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.TextView["
                                                        "@resource-id='com.google.android.youtube:id/title']")
        print("Current Logged In User : {0} ".format(logged_user.get_attribute('text')))
        if logged_user.get_attribute('text') == "champak.7000@gmail.com":
            print('User already Logged in !')
        else:
            accountlist = []
            lst = self.driver.find_elements_by_xpath("//android.widget.TextView["
                                                     "@resource-id='com.google.android.youtube:id/title']")
            for value in lst:
                ele_name = value.get_attribute('text')
                accountlist.append(ele_name)
            print('List of Accounts Added : '.format(accountlist))
            if 'champak.7000@gmail.com' in accountlist:
                try:
                    self.driver.find_element_by_xpath(
                        "//android.widget.LinearLayout[@content-desc='Tuli Bandra']").click()
                except Exception as e:
                    print("Element could not be located ", e)

    @pytest.mark.skip
    def test_03_videoPlayback(self):
        # Select Video
        print('------------Running Video Playback test--------------- ')
        video = self.driver.find_element_by_xpath("//android.view.ViewGroup[@index='1']")
        time.sleep(1)
        print('Playing video {0}'.format(video.get_attribute('content-desc')))
        video.click()
        time.sleep(4)

        # Checking Video Playback
        time.sleep(5)
        TouchAction(self.driver).tap(x=361, y=217).perform()
        self.driver.find_element_by_accessibility_id('Pause video').click()
        t1 = self.driver.find_element_by_xpath("//android.widget.TextView["
                                               "@resource-id='com.google.android.youtube:id/time_bar_current_time']").get_attribute(
            'text')
        t3 = t1.replace(':', '.')
        self.driver.find_element_by_accessibility_id('Play video').click()
        time.sleep(5)
        TouchAction(self.driver).tap(x=361, y=217).perform()
        time.sleep(1)
        self.driver.find_element_by_accessibility_id('Pause video').click()

        t2 = self.driver.find_element_by_xpath("//android.widget.TextView["
                                               "@resource-id='com.google.android.youtube:id/time_bar_current_time']").get_attribute(
            'text')
        t4 = t2.replace(':', '.')
        if float(t4) > float(t3):
            print('Video is Playing')
        else:
            print('Check Code--')

    @pytest.mark.skip
    def test_04_search(self):
        self.driver.find_element_by_accessibility_id('Search').click()
        search_text = self.driver.find_element_by_xpath("//android.widget.EditText["
                                                        "@resource-id='com.google.android.youtube:id/search_edit_text']")
        search_text.send_keys(YoutubeTestCases.text)
        self.driver.press_keycode(66)  # Enter
        resultlist = []
        time.sleep(1)
        lst = self.driver.find_elements_by_xpath("//android.view.ViewGroup")
        for value in lst:
            ele_name = value.get_attribute('content-desc')
            if ele_name is not None:
                resultlist.append(ele_name)
        print('Search Result :: {0} '.format(resultlist))
        time.sleep(2)
        self.assertTrue(any(YoutubeTestCases.text in result.lower() for result in resultlist), msg='Value Not Matched')

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
