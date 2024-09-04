"""
高级特性
"""
from collections.abc import Iterable

print("###### 切片 ######")
print("###### 列表切片 ######")
L = ["a", "b", "c", "d"]
print(L)
print(f'L[1:3]:{L[1:3]}')
print(f'L[:3]:{L[:3]}')
print(f'L[:-1]:{L[:-1]}')
print(f'L[-2:]:{L[-2:]}')

L = list(range(100))
print(L)
print(f'L[10:21]:{L[10:21]}')
print(f'L[:10:2]:{L[:10:2]}')
print(f'L[80::2]:{L[80::2]}')

print("###### 元组切片 ######")
T = 0, 1, 2, 3, 4, 5
print(T)
print(f'T[1:3]:{T[1:3]}')

print("###### 字符串切片 ######")
S = "hello world"
print(S)
print(f'S[:5]:{S[:5]}')
print(f'S[5:6]:{S[5:6]}')
print(f'S[6:]:{S[6:]}')

print("###### 迭代 ######")
# list
for ele in ['a', 'b']:
    print(ele)
# tuple
for ele in 'a', 'b':
    print(ele)
# set
for ele in ('a', 'b'):
    print(ele)
# dict
dict_0 = {'a': 1, 'b': 2}
for key in dict_0:
    print(key, dict_0[key])
    
for val in dict_0.values():
    print(val)
    
for key, val in dict_0.items():
    print(key, val)
# str
for chr in "ABC":
    print(chr)

# 是否支持迭代
print(isinstance(dict_0, Iterable))

# 迭代时能够获取索引
for index, val in enumerate(['a', 'b']):
    print(index, val)
    
# 单个元素也为迭代类型的数据，可一次性获取该数据的值
for x, y in [[1, 2], [3, 4], (13, 9)]:
    print(x, y)
    
def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    if len(L) == 1:
        return L[0], L[0]
    min = L[0]
    max = L[0]
    for ele in L:
        if ele < min:
            min = ele
        if ele > max:
            max = ele
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')