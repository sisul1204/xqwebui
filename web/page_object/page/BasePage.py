#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/8/25 9:02
# file: BasePage.py
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver):
        self.driver:WebDriver = driver