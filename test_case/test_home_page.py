# -*- coding: utf-8 -*-
#python3.7
#liguanhao

from common.driver_configure import configure
from PO.home_page import HomePage
from common.base_page import Action
import unittest
import time

class Test(unittest.TestCase):

    def setUp(self):
        dconfigure = configure()
        self.driver = dconfigure.get_driver()

        time.sleep(10)
        if self.driver.find_element_by_xpath("//*[@text='同意']").is_displayed():
            self.driver.find_element_by_xpath("//*[@text='同意']").click()
        else:
            print("无注册协议弹窗")

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        print("测试用例1")
        time.sleep(5)
        a = HomePage(self.driver)
        a.KuaiJieJiaYou()



