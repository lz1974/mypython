# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
作者：huilan_same
来源：CSDN
原文：https://blog.csdn.net/huilan_same/article/details/52944782
版权声明：本文为博主原创文章，转载请附上博文链接！
'''



import  unittest
from test_mathfunc import TestMathFunc
if __name__ == '__main__':

    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus")]
    suite.addTests(tests)# 直接用addTest方法添加单个TestCase

    '''
    # 用addTests + TestLoader
    # loadTestsFromName()，传入'模块名.TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    suite.addTests(
    unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表
    '''    '''
    # loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
'''
with open('UnittestTextReport.txt', 'a') as f:   # 结果生成到了UnittestTextReport
    runner = unittest.TextTestRunner(stream=f,verbosity=2)
    runner.run(suite)
