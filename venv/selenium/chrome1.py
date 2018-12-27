import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs

#driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
driver = webdriver.Chrome()
driver.get("http://www.sxlm123.com/exam/login.jsp")
# wait = driver.wait(driver, 10)  # 等待的最大时间
print(driver.title)
assert "书香联萌管理平台" in driver.title  # 断言
driver.implicitly_wait(600)
#driver.find_element_by_id('uid').send_keys("qatest")
driver.find_element_by_xpath("//*[@id='uid']").send_keys("qatest")
driver.find_element_by_xpath("//*[@id='pwd']").clear()
driver.find_element_by_xpath("//*[@id='pwd']").send_keys("qatest")
driver.find_element_by_xpath("/html/body/form/div[2]/div/div[1]/div/input[4]").click()
driver.find_element_by_class_name("tjts menu-item").click()
#adriver.find_element_by_id('pwd').clear()
#adriver.find_element_by_id('pwd').send_keys("qatest")
#adriver.find_element_by_class_name("btbg_login").click()
#aprint(driver.title)

#assert "书香联萌" in driver.title  # 断言
#driver.find_element_by_class_name("glzx menu-item").click()
assert "No results found." not in driver.page_source  #为了确保某些特定的结果被找到，使用`assert`如下




















