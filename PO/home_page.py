# -*- coding: utf-8 -*-
#python3.7
#liguanhao
from common import base_page
from selenium.webdriver.support.ui import WebDriverWait
from common.driver_configure import configure


class HomePage(base_page.Action):
    kuaijiejiayou_loc = "快捷加油"


    def KuaiJieJiaYou(self):
        self.By_xpath(self.kuaijiejiayou_loc).click()




