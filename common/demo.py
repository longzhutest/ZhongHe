# -*- coding: utf-8 -*-
#python3.7
#liguanhao

from selenium.webdriver.support.ui import WebDriverWait
import unittest
import selenium
import time
from appium import webdriver

class MyTestCase(unittest.TestCase):

    #配置设置
    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-55544'
        desired_caps['appPackage'] = 'com.ibona.energy'
        # desired_caps['app'] = 'F:// debug.apk'
        desired_caps['appActivity'] = 'com.ibona.energy.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        #判断有没有用户注册协议弹窗
        time.sleep(10)
        if self.driver.find_element_by_xpath("//*[@text='同意']").is_displayed():
            self.driver.find_element_by_xpath("//*[@text='同意']").click()
        else:
            pass

    # @unittest.skip
    # def test_01(self):
    #     print("测试用例1")
    #     time.sleep(5)
    #     self.driver.find_element_by_name("我的").click()
    #     time.sleep(5)

    # @unittest.skip
    # def test_02(self):
    #     print("测试用例2")
    #     time.sleep(10)
    #     if self.driver.find_element_by_xpath("//*[@text='同意']").is_displayed():
    #         self.driver.find_element_by_xpath("//*[@text='同意']").click()
    #     else:
    #         pass

    # def test_03(self):
    #     loc = "我的"
    #     loc_xiaoxi = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView"
    #
    #     print("测试用例3")
    #     time.sleep(10)
    #     self.driver.find_element_by_xpath("//*[@text='%s']"%loc).click()
    #     time.sleep(5)
    #     # self.driver.find_element_by_xpath("android.widget.ImageView").click()
    #     # self.driver.find_elements_by_xpath(loc_xiaoxi).click()
    #     self.driver.find_elements_by_xpath("//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[contains(@index,0)]").click()
    #
    #     time.sleep(5)
    #
    def test_04(self):
        loc = "快捷加油"
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@text='%s']"%loc).click()





    @classmethod
    def tearDown(self):
        time.sleep(5)
        print('tearDown ------ ')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()