import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Keys 类提供所有的键盘按键操作

class PythonOrgSearch(unittest.TestCase): #该测试类继承自 unittest.TestCase.
    def setUp(self): #setUp()方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库连接并进行初始化。如测试用例需要登录web，可以先实例化浏览器。该方法会在该测试类中的每一个测试方法被执行前都执行一遍。
        self.driver=webdriver.Chrome()
    def test_search_in_Baidu(self):
        driver=self.driver
        driver.get("http://www.baidu.com")
        wait = WebDriverWait(browser, 10)  # 等待的最大时间
        print(driver.title)
        assert "a" in driver.title # 断言
        driver.implicitly_wait(10)

def tearDown(self): #tearDown()方法用于测试用例执行之后的善后工作。如关闭数据库连接。关闭浏览器。
    self.driver.close()

if __name__ == "__main__":   # 入口函数
    unittest.main()