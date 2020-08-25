#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/8/25 14:36
# file: test_864.py

from selenium import webdriver
from time import sleep

class Test864:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://max-bim.com:864")
        self.driver.maximize_window()

    def test_login(self):
        self.driver.add_cookie({"name":"token", "value":"d40c38ad26fe0c2bfec88dc23bfa2290"})
        self.driver.
        # self.driver.add_cookie({"name":"userinfo", "value":'{"id":660,"token":"d40c38ad26fe0c2bfec88dc23bfa2290","name":"tester","headimg":"","com_id":0,"type":4,"email":"","street_id":168,"tel":"15611112222","job":"","permission_json":"","street_name":"测试街道","company_name":""}'})
        print(self.driver.get_cookies())
        self.driver.refresh()
        sleep(2)
        self.driver.get('https://max-bim.com:864/#/commandCenter')


    def teardown(self):
        sleep(5)
        self.driver.quit()

