'''
发送post请求
    1.使用data传表单格式传送
'''
import requests
# 发送post请求，代参数时，可以使用date或json开传参，具体使用哪个要看系统怎么实现的
# 上一步注册成功的手机号，验证登录，登录使用post
url = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"13812345678","pwd":"123456"}
r = requests.post(url,data = canshu)#表单
print(r.text)
url = "http://jy001:8081/futureloan/mvc/api/member/login"#金融系统不支持json方式传送
r = requests.post(url,json = canshu)
print(r.text)