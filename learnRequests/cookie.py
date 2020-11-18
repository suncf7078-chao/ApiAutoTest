'''
cookie
'''

import requests


# head = {
#
# }
# r = requests.get("https://www.bagevent.com/account/dashboard",heads = head)
# print(r.text)

'''
requests 中自动管理cookies的机制
'''
s = requests.session() #创建了一个session，通过session发送请求
print("登录之前的cookies",s.cookies)
# 登录D:\python\python3.8\Lib
canshu = {
    "access_type":1,
    "loginType":1,
    "emailLoginWay":0,
    "account":"3109587887@qq.com",
    "password":"sun1997...",
    "remindmeBox":"on",
    "remindme":1
}
r = s.post("https://www.bagevent.com/user/login",headers = canshu)
print(r.text)
print("登录之后的cookies",s.cookies)
r = s.get("https://www.bagevent.com/account/dashboard")
print("<title>百格活动 - 账号总览</title>" in r.text)