# -*- coding:utf-8 -*-

'''本段代码非淘宝，而是本人实际操作的app'''
import os
import time
import unittest

from appium  import webdriver


PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '4.4.4'  # 设备系统版本
desired_caps['deviceName'] = '83c99b30'  #  设备名称

desired_caps['app'] = PATH(r"E:\书香联萌SVN\书香联萌\3.测试\测试版本\四川文轩1016\book.apk") # 设备有APP无需安装
desired_caps['appPackage'] = 'com.HB.book'
desired_caps['appActivity'] = 'com.HB.book.MainActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)




