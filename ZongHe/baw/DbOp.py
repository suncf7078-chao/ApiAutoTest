'''
数据库操作
1.数据库从mysql换成sqlite，脚本层不用改动，只需要改动mysqlop.py以及这个文件
这部分访问到业务的数据库了，所以放baw中
'''
from ZongHe.caw import MySqlOp


def deleteUser(db,phone):
    '''
    根据手机号删除用户
    :param db: 一个字典，储存数据库信息
    :param phone: 手机号
    :return:
    '''
    conn = MySqlOp.connect(db)
    MySqlOp.execute(conn,f'delete from Member where MobilePhone = {phone}')
    MySqlOp.disconnect(conn)