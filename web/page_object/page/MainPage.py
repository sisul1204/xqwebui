#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/8/25 9:03
# file: MainPage.py
from web.page_object.page.BasePage import BasePage
from web.page_object.page.SearchPage import SearchPage


class MainPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_name('q').send_keys(keyword)
        self.driver.find_element_by_css_selector('.Header_nav__search_1YZ button').click()
        return SearchPage(self.driver)
