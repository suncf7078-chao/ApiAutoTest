"""
监控代码：监控服务器的内存，cpu，网络，磁盘等等，与租车系统部署在一起
"""

import psutil

print(psutil.cpu_count())  # 获取CPU信息
print(psutil.virtual_memory())  # 虚拟内存
print(psutil.virtual_memory().percent)  # 虚拟内存百分比
print(psutil.disk_usage("d:/"))  # 租车系统所在磁盘
print(psutil.disk_usage("d:/").percent)  # 租车系统所在磁盘的百分比
print(psutil.net_io_counters())  # 网络
print(psutil.net_io_counters().bytes_sent)  # 发送字节数
print(psutil.net_io_counters().bytes_recv)  # 接受字节数

# 达到类似serveragent的效果，在性能测试期间，获取cpu、内存的趋势
# 死循环，每隔3s读一次，把读的结果写到文件中，测试结束后分析文件，使用excel等生成图像
# 时间戳 cpu% 内存% 磁盘% 发送字节数 接受字节数