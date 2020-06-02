# -*- coding: utf-8 -*-
#python3.7
#liguanhao

from appium import webdriver

class configure():

    #配置设备参数
    def get_driver(self):
        try:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator'
            desired_caps['appPackage'] = 'com.ibona.energy'
            # desired_caps['app'] = 'F:// debug.apk'
            desired_caps['appActivity'] = 'com.ibona.energy.MainActivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            return self.driver
        except Exception as e :
            raise e
