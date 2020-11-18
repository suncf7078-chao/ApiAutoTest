'''
上传文件，一般都是post接口，用file参数上传文件
'''

import requests

url = "http://www.httpbin.org/post"

'''
files参数，字典格式，’name‘：file-tuple
file-tuple可以是2=tuple（’filename‘，fileobj）、3-tuple（’filename‘，fileobj，’content_type‘）,4-tuple
'''
# with open("E://恢复密钥G//test.txt",encoding="utf-8") as f:
#     file = {"file1":("test.txt",f,"text/plain")}
#     r= requests.post(url,files=file)
#     print(r.text)
#
# # 上传一个图片文件
#
# with open("E://恢复密钥G//号码.jpeg",mode = 'rb') as f:
#     file = {"file1":("号码.jpeg",f,"imafe/jpeg")}
#     r = requests.post(url,files = file)
#     print(r.text)

# 一次上传多个文件
with open("E://恢复密钥G//test.txt",encoding = 'utf-8') as f:
    with open("E://恢复密钥G//号码.jpeg", mode='rb') as l:
        file = {"file1":("test.txt",f,"text/plain"),"file2":("号码.jpeg",l,"imafe/jpeg")}
        r = requests.post(url,files = file)
        print(r.text)