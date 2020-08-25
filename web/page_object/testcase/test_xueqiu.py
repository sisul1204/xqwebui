#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/8/25 8:43
# file: test_xueqiu.py
from selenium import webdriver

from web.page_object.page.MainPage import MainPage
from time import sleep

class TestXueqiu:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://xueqiu.com')
        self.driver.maximize_window()
        self.main = MainPage(self.driver)

    def test_search(self):
        self.main.search('alibaba').follow('BABA')
        #todo assertion


    def test_profile(self):
        print(self.driver.get_cookies())
        self.driver.add_cookie({"name":"device_id", "value":"24700f9f1986800ab4fcc880530dd0ed"})
        self.driver.add_cookie({"name": "Hm_lvt_1db88642e346389874251b5a1eded6e3", "value": "1596590789,1598339972,1598341124"})
        self.driver.add_cookie({"name": "snbim_minify", "value": "true"})
        self.driver.add_cookie({"name": "s", "value": "dr11ouwgsj"})
        self.driver.add_cookie({"name": "xq_a_token", "value": "072d727c267ff2ecd93c043addc6c9ee836bdebb"})
        self.driver.add_cookie({"name": "xqat", "value": "072d727c267ff2ecd93c043addc6c9ee836bdebb"})
        self.driver.add_cookie({"name": "xq_r_token", "value": "30401101fa1644a133f139e6e7038be01acd58fd"})
        self.driver.add_cookie({"name": "xq_id_token", "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUyNjYxODIxOTMsImlzcyI6InVjIiwiZXhwIjoxNjAwOTEzODU3LCJjdG0iOjE1OTgzMzk5NzYzMDcsImNpZCI6ImQ5ZDBuNEFadXAifQ.DmkVtDzWM66xtjQ_HDJZlez9Lb7gSAm1FCCKjIzZeseCE33NwyQSUqpOJ1chEOJJh0xneaMubv_5b-a-MSQ5YbpxNgCPY28JZHLzSoTdS9UpbuVU8asfl-BYNtWV74WtWchXHC71CHBpIhKeDkfuUb0LXN_qzXA0cy3SHzHbsu3Y7c_LnxVJxp_F58xHaGIWFXymdswMTXx5cyfkGPhCEf4dcIdwJoSHaBgeXgAOYpPqfszmsK1BGdCuJx5yunC9Wcio4PSCzxrGgmrE9aAebpjA0KOnrpodplJI_x_r4Gx4Tgdf4lwgQuypfPvZEazKVe0pzVIdz585FpY3X29IhA"})
        self.driver.add_cookie({"name": "xq_is_login", "value": "1"})
        self.driver.add_cookie({"name": "u", "value": "5266182193"})
        self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "1598341124"})
        self.driver.add_cookie({"name":"acw_tc", "value":"2760820415983399702132178edcb3880c05510179473a12cffd1bad66bc08"})
        self.driver.add_cookie({"name":"bid", "value":"06dfb95ef65ac231d6aed79bbc7c6b4c_ke9mcyk7"})
        self.driver.add_cookie({"name":"is_overseas", "value":"0"})
        # self.driver.add_cookie({"name": "__utma", "value": "1.67285074.1598339988.1598339988.1598339988.1"})
        # self.driver.add_cookie({"name": "__utmc", "value": "1"})
        # self.driver.add_cookie({"name": "__utmz", "value": "1.1598339988.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"})
        # self.driver.add_cookie({"name": "__utmb", "value": "1.1.10.1598339988"})


        print(self.driver.get_cookies())
        self.driver.get('https://xueqiu.com/setting/user')



    def teardown(self):
        sleep(10)
        self.driver.quit()