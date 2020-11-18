"""
性能测试
"""

from locust import HttpUser, between

'''
1.为要模拟的用户定义一个类，从httpuser继承
'''





class CarRental(HttpUser):
    # betwen 是user类中定义的一个方法
    # wait_time 是user类定义的一个属性，表示等待时间
    wait_time = between(3, 8)  # 任务跟任务之间的等待时间在3~8之间取随机数

    @task
    def loadAllRent(self):
        #
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllMenu(self):
        self.client.get("/carRental/menu/loadAllRent.action?page=1&limit=10")


# -f 要执行的文件
# --host 被测系统
# --web-host locust Web页面的访问地址
# --web-port locust Web页面的访问端口
# locust _f locust_test.py --loca=lo:3306
