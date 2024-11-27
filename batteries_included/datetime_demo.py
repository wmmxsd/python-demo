from datetime import datetime, timezone, timedelta

print('datetime.now():', datetime.now())

print('datetime(2024, 10, 1, 22, 22, 22):', datetime(2024, 10, 1, 22, 22, 22))

# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp
epoch = datetime(1970, 1, 1, tzinfo = timezone.utc)
epoch1 = datetime(1970, 1, 1, 0, 1, 5, tzinfo = timezone.utc)
print(epoch.timestamp())
print(epoch1.timestamp())

# timestamp转换为datetime
print(datetime.fromtimestamp(3665, tz = timezone.utc))

# 字符串转换为datetime
print(datetime.strptime('2024-10-01T00:00:00', '%Y-%m-%dT%H:%M:%S'))

# datetime转换为字符串
print(r'''datetime.now().strftime('%Y-%m-%d %H:%M:%S'):''', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(r'''datetime.now().strftime('%Y-%m-%d 00:00:00'):''', datetime.now().strftime('%Y-%m-%d 00:00:00'))
print(r'''datetime.now().strftime('%Y-%m-%d 23:59:59'):''', datetime.now().strftime('%Y-%m-%d 23:59:59'))

# datetime加减
print('datetime.now() + timedelta(days = 1):', datetime.now() + timedelta(days = 1))
print('datetime.now() + timedelta(days = -1):', datetime.now() + timedelta(days = -1))
print('datetime.now() + timedelta(weeks = -1):', datetime.now() + timedelta(weeks = -1))
print('datetime.now() + timedelta(weeks = 1):', datetime.now() + timedelta(weeks = 1))

# 本地时间转换为UTC时间
tz_utc_0 = timezone(timedelta(hours = 0))
# 创建UTC+8:00时区
tz_utc_8 = timezone(timedelta(hours = 8))
tz_utc_4 = timezone(timedelta(hours = 4))
now = datetime.now()
print('now:', now)
print('now.now(tz_utc_0):', now.now(tz_utc_0))
print('now.now(tz_utc_8):', now.now(tz_utc_8))
# 时区从东八区换成东四区后，小时数未变
print('now.replace(tzinfo = tz_utc_4):', now.replace(tzinfo = tz_utc_4))

# 时区转换
now_utc = datetime.now(timezone.utc)
print('datetime.now(timezone.utc):', now_utc)
now_utc_9 = now_utc.astimezone(timezone(timedelta(hours=9)))
print('now_utc.astimezone(timezone(timedelta(hours = 9))):', now_utc_9)
print('now_utc_9.astimezone(tz_utc_8):', now_utc_9.astimezone(tz_utc_8))

