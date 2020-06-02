# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time

testcase_path = "./"
now = time.strftime("%Y-%m-%d %H-%M-%S")
report_path = "./report/"+ now +"test_result.html"

def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit

suite = creat_suite()
fp = open(report_path,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="jimitest", description="baogao")
runner.run(suite)
fp.close()
