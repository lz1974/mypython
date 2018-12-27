# -*- coding:utf-8 -*-

'''本段代码非淘宝，而是本人实际操作的app'''
import os
import time
import unittest

from appium  import webdriver


PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '5.0.2'  # 设备系统版本
desired_caps['deviceName'] = '4bbd8cf0'  #  设备名称

desired_caps['app'] = PATH(r"E:\书香联萌SVN\书香联萌\3.测试\测试版本\四川文轩1016\book.apk") # 设备有APP无需安装
desired_caps['appPackage'] = 'com.HB.book'
desired_caps['appActivity'] = 'com.HB.book.MainActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


time.sleep(30)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View")
el1.click()



