import pymysql.cursors
# Connect to the database

db = pymysql.connect(host='192.168.3.242',user='root',password='pwd123456',db='mproduct',charset='utf8',connect_timeout=10)
cursor = db.cursor()
# SQL 查询语句
sql = "select * from tuser where id=46138"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()  #将查询结果返回成一个元组
    print(results)
    for row in results:
        id = row[0]
        # 打印结果
        print("id=%s" % (id))
except:
    print("Error: unable to fecth data")

# 关闭数据库连接
cursor.close()
db.close()