
import requests
import unittest
import json

class test(unittest.TestCase):

    def test_login_api(self):
        url = "http://192.168.3.244:8201/user/login"
        payload1 = {'userid': 'hbtestmanage', 'pwd': '4SWD4G6P4M'}
        payload2 = {'userid': 'hbtestmanage'}
        payload3 = {'pwd': '4SWD4G6P4M'}
        response = requests.request("post", url, params=payload1).json()
        data=response['data']
        # response = requests.request("post", "http://192.168.3.244:8201/user/login", params=payload1).json()
        print(response)
        print(data['id'])

        # print(text)
        #self.assertEqual(response['code'], 0)
        #self.assertEqual(response['message'], '登录成功')
        #self.assertEqual(response['data']['id'], 46138)
        #print(response)



if __name__ == '__main__':
    unittest.main()
