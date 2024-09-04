"""
if else、match case、循环
"""
nums = input('请输入您的体重（kg）：')
while nums is None or not nums.isdigit():
    nums = input('输入的不是数字，请重新输入您的体重：')

weight = int(nums)

print('######if else######')
if weight < 100:
    print('too thin')
    print('you need eating')
elif weight <= 130:
    print('normal')
else:
    print('too fat')
    print('you need slimming')

print('\n######match case######')
match weight:
    case x if x < 100:
        print('too thin')
        print('you need eating')
    case  x if x <= 130:
        print('normal')
    case  _:
        print('too fat')
        print('you need slimming')

args = ['gcc', 'hello.c', 'world.c', 'python.c']
# args = ['clean']
# args = ['gcc']
match args:
    case ['gcc']:
        print ('gcc: missing source files.')
    #第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files，它实际上表示至少指定一个文件
    case ['gcc', *files]:
        print (f'gcc compile: {", ".join(files)}')
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

print('\n######loop######')
print('\n######loop-for in######')
names = ['a', 'b', 'c']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)
print(f'list(range(5)):{list(range(5))}')
sum = 0
for x in list(range(101)):
    sum += x
print(sum)
print('\n######loop-for while######')
sum = 0
n = 1
while n < 101:
    sum += n
    n = n + 1
print(sum)
sum = 0
n = 0
while n < 101:
    n = n + 1
    if n < 10:
        continue
    sum += n
print(sum)

