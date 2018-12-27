import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.sxlm123.com.cn/sxlm_manage/#/login")

print(driver.title)
#assert "后台管理系统" in driver.title  # 断言

#driver.find_element_by_id('uid').send_keys("qatest")
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/form/div[1]/div/div[1]/input").clear()
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/form/div[1]/div/div[1]/input").send_keys("linxz")
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/form/div[2]/div/div[1]/input").clear()
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/form/div[2]/div/div[1]/input").send_keys("999999")


driver.find_element_by_xpath("//*[@id='app']/div/div[2]/form/div[3]/button").click()



#driver.find_element_by_xpath("//*[@id='pwd']").clear()
#driver.find_element_by_xpath("//*[@id='pwd']").send_keys("qatest")
#driver.find_element_by_xpath("/html/body/form/div[2]/div/div[1]/div/input[4]").click()
#driver.find_element_by_class_name("tjts menu-item").click()
#driver.quit()





















