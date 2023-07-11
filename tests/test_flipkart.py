import unittest
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from base.BasePage import BasePage
from base.Driver import Driver


@pytest.mark.usefixtures("setUpFlipkart", "initialSetupFlipkart")
class TestFlipkartCases(unittest.TestCase):
    # driver = Driver.getDriver('com.flipkart.android', 'com.flipkart.android.activity.HomeFragmentHolderActivity')

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.page = BasePage(self.driver)

    @pytest.mark.skip
    def test_01_isAppInstalled(self) -> None:
        print("=============== Check if App is installed ================")
        assert self.driver.is_app_installed('com.flipkart.android')

    @pytest.mark.skip
    def test_02_search(self) -> None:
        ele_search_for_product = self.page.waitForElement('text', "Search for products")
        ele_search_for_product.click()
        ele_search_text = self.page.waitForElement('class', "android.widget.EditText")
        ele_search_text.send_keys("shoes")
        self.driver.press_keycode(66)
        ele_product = self.page.waitForElement('xpath', '//android.view.ViewGroup/android.view.ViewGroup['
                                                        '2]/android.view.ViewGroup/android.view.ViewGroup['
                                                        '1]/android.view.ViewGroup[1]/android.widget.ImageView['
                                                        '1]')
        ele_product.click()
        self.page.scrollIntoView("All Questions")
        ele_all_ques = self.page.waitForElement('text', "All Questions")
        ele_all_ques.click()
        ele_result = self.page.waitForElement('id', "com.flipkart.android:id/title_action_bar")
        self.assertEqual(ele_result.text, "Questions and Answers")

    @pytest.mark.skip
    def test_03_openNotification(self) -> None:
        self.driver.open_notifications()
        seekBar = self.driver.find_element(AppiumBy.ID, value="com.android.systemui:id/slider")
        seekBar.send_keys("6000")
        self.driver.implicitly_wait(1000)

    def test_addToCart(self):
        ele_search_for_product = self.page.waitForElement('text', "Search for products")
        ele_search_for_product.click()
        ele_search_text = self.page.waitForElement('class', "android.widget.EditText")
        ele_search_text.send_keys("shoes")
        self.driver.press_keycode(66)
        ele_product = self.page.waitForElement('xpath', '//android.view.ViewGroup/android.view.ViewGroup['
                                                        '2]/android.view.ViewGroup/android.view.ViewGroup['
                                                        '1]/android.view.ViewGroup[1]/android.widget.ImageView['
                                                        '1]')
        ele_product.click()
        ele_selected = self.page.waitForElement('xpath',
                                                "//android.view.ViewGroup/android.view.ViewGroup["
                                                "4]/android.view.ViewGroup/android.widget.TextView")
        ele_selected_text = ele_selected.text
        print(ele_selected_text)
        add_cart = self.page.waitForElement('text', "Add to cart")
        add_cart.click()
        ele_size = self.page.waitForElement('text', "6")
        ele_size.click()
        ele_continue = self.page.waitForElement('text', "Continue")
        ele_continue.click()
        # toast = self.driver.find_element(AppiumBy.XPATH, value="//android.widget.Toast")
        # print(f'Toast msg ::  {toast.text}')
        self.driver.implicitly_wait(5000)
        go_to_cart = self.page.waitForElement('text', "Go to cart")
        go_to_cart.click()

        ele_in_cart = self.page.waitForElement('xpath', "//android.view.ViewGroup/android.view.ViewGroup["
                                                        "2]/android.view.ViewGroup/android.view.ViewGroup["
                                                        "3]/android.widget.TextView[1]")
        ele_in_cart_text = ele_in_cart.text
        print(ele_in_cart_text)
        self.assertIn(ele_in_cart_text, ele_selected_text)
