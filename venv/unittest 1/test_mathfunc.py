# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
作者：huilan_same
来源：CSDN
原文：https://blog.csdn.net/huilan_same/article/details/52944782
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
import unittest
from mathfunc import add
from mathfunc import minus
from mathfunc import multi
from mathfunc import divide
class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(4, add(1, 2))
        self.assertNotEqual(3, add(2, 2))


    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
    '''
    在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，
    #默认是 1，如果设为 0，则不输出每一用例的执行结果，
    #即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果，如下：
'''