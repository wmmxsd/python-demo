"""
psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块
"""
import time

import psutil

print('CPU物理核心数量：', psutil.cpu_count(logical=False))
print('CPU逻辑数量：', psutil.cpu_count())
print('CPU频率：', psutil.cpu_freq())

for index in range(2):
    print('CPU利用率：', psutil.cpu_percent(interval=0.5), '%')

# 物理内存： svmem(total=17044447232（bit）, available=5690527744, percent=66.6, used=11353919488, free=5690527744)
print('物理内存：', psutil.virtual_memory())
print('交换内存：', psutil.swap_memory())

print('网卡：', psutil.net_if_addrs())
print('硬盘分区：', psutil.disk_partitions())
print('C盘使用情况：', psutil.disk_usage('C:\\'))

print('当前用户：', psutil.users())

print(psutil.pids())
# print(psutil.wait_procs([psutil.Process(15340)]))
print(psutil.pid_exists(1780))
for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    print(f'{p.name():>40s} {p.pid:>5d} {p.memory_percent():>1f}%')

