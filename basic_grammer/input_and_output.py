"""
系统输入和输出
"""
print (200 + 300)
print ('###########')
a = 100
if a >= 101:
    print(a)
elif a == 100:
    print(a + 1)
    print(a + 2)
else:
    print(a + 3)
print ('###########')
name = input('请输入姓名：')
sex = input('请输入性别：')
while sex != "男" and sex != '女':
    print('性别输入错误，请重新输入')
    sex = input('请输入性别：')
age = input('请输入年纪：')
print(name, '：', sex, '，', age, '岁')
