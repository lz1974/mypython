import flask
from flask import jsonify
from conf import opRedis
from flask import request

'''
读取redis内的数据，redis数据存储类型是hash类型，格式如下
{name:{"key":"value"}}
思路： 1.通过redis的hgetall(name)方法读取redis所有数据，返回结果类型是字典
 2. 循环字典内容，将元素类型转换为str，并将结果存放到字典内
'''
server = flask.Flask(__name__)


@server.route('/get_sties', methods=['get', 'post'])
def get_sties():
    # 获取redis内所有的数据信息，返回结果类型是字典，里面元素是bytes类型，name=sites
    dic = opRedis.get_hashall('sites')
    redisList = []
    for key, value in dic.items():
        redis_dic = {}
        # 将字典内元素的类型由bytes转换为str
        k = key.decode()
        v = value.decode()
        # 字典redis_dic内结构{"username:k, "url":v}
        redis_dic['username'] = k
        redis_dic['url'] = v
        redisList.append(redis_dic)
    return jsonify({"code": 200, "msg": redisList})


if __name__ == '__main__':
    # port可以指定端口，默认端口是5000
    # host默认是127.0.0.1,写成0.0.0.0的话，其他人可以访问，代表监听多块网卡上面，
    server.run(debug=True, port=8899, host='0.0.0.0')