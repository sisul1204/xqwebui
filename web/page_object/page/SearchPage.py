#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/8/25 9:18
# file: SearchPage.py
from web.page_object.page.BasePage import BasePage


class SearchPage(BasePage):

    def follow(self, keyword):
        self.driver.find_element_by_xpath('//*[span="%s"]/../../..//*[@class="iconfont"]' % keyword).click()
        return self
