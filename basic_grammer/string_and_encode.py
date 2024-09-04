"""
字符串、编码和反编码
"""
#在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言。
#Unicode编码用2个字节代表1个字符，支持所有语言比如中文、日文、韩文、英语等等。
print ('###########')
print ('中文English')
print ('###########')
#ord()方法获取字符的数字表示
print ('###########')
print ('ord(\'A\'):', ord('A'))
print ('###########')
#chr()将数字转为字符串
print ('###########')
print ('chr(65):', chr(65))
print ('###########')
#字符串和字节相互转换
print ('###########')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print ('###########')
#len()获取字符串长度
print ('###########')
print('SONY无线耳机字符长度：', len('SONY无线耳机1'))
print ('###########')
#格式化
print ('###########')
print('%s您好！今天是%s' % ('Tom', '2024-9-3 11:08:08'))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415)
print('increase %.3f%%' % 10.12345)
print ('###########')
#f-string(一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换)
print ('###########')
R = 2
S = 3.14 * R ** 2
print(f'半径为{R:03d}cm的圆的面积为{S:.4f}cm\'2')
S1 = 72
S2 = 85
print('小明的成绩提升率为：%.3f%%' % ((S2-S1) / S1))
print(f'小明的成绩提升率为：{((S2-S1) / S1):.3f}%')
print ('###########')
