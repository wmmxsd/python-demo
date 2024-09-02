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
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')
print ('###########')