# -*- coding: utf-8 -*-
#python3.7
#liguanhao

from selenium.webdriver.support.ui import WebDriverWait
import unittest
import selenium
import time
import appium

from appium import webdriver

#封装查询元素方法
class Action(object):

    def __init__(self,se_driver):
        self.driver = se_driver

    def By_id(self,loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element_by_id(loc))
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("找不到元素%s"%(loc))

    def By_name(self,loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element_by_name(loc))
            return self.driver.find_element_by_name(loc)
        except Exception as e:
            print("找不到元素%s"%(loc))

    def By_xpath(self,loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath("//*[@text='%s']"%loc))
            return self.driver.find_element_by_xpath("//*[@text='%s']"%loc)
        except Exception as e:
            print("找不到元素%s" % (loc))

    def UserRegistration(self):
        time.sleep(10)
        if self.driver.find_element_by_xpath("//*[@text='同意']").is_displayed():
            self.driver.find_element_by_xpath("//*[@text='同意']").click()
        else:
            pass