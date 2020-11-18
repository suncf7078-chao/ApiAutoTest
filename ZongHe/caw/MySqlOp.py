'''
数据库操作
'''
import pymysql


# 链接数据库
def connect(db):
    '''
    链接数据库
    :param db:
    :return:
    '''
    global conn
    host = db['ip']
    port = db['port']
    user = db['username']
    name = db['dbName']
    pwd = db['pwd']
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=name, charset="utf8")
        print(f"链接数据库：{host}:{port}成功")
    except Exception as e:
        print(f"链接数据库异常，异常信息为:{e}")
    return conn


# 断开数据库链接
def disconnect(conn):
    try:
        conn.close()
        print(f"断开数据库链接成功")
    except Exception as e:
        print(f"断开数据库链接失败，异常信息为：{e}")


# 执行sql语句
def execute(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        print(f"执行sql语句{sql}成功")
    except Exception as e:
        print(f"执行sql语句{sql}失败，异常信息为：{e}")


if __name__ == '__main__':
    db = {"ip": "jy001", "port": 4406, "dbName": "future", "username": "root", "pwd": "123456"}
    conn = connect(db)
    execute(conn, "delete from Member where MobilePhone = 1801234567")
    disconnect(conn)
