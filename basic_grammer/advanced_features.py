"""
高级特性
"""
from collections.abc import Iterable
import os

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

print("###### 列表生成式 ######")
# 利用[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]生成[1x1, 2x2, 3x3, ..., 10x10]
# 方法1
L = []
print(L)
for x in list(range(1, 11)):
    L.append(x * x)
print(L)
# 方法2（列表生成式，更简洁）
L = [x * x for x in list(range(1, 11))]
print(L)
# 列表生成式后面可以接if判断
L = [x * x for x in list(range(1, 11)) if x % 2 == 0]
print(L)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str)]
print(L2)
# 列表生成式for前面可以接if else表达式
L = [x * x  if x % 2 == 0 else -x for x in list(range(1, 11))]
print(L)
# 列表生成式支持多层循环
L = [m + '-' + n for m in 'ABC' for n in '123']
print(L)
L = [m + '-' + n + '-' + o for m in 'ABC' for n in '123' for o in ('0', '1', '1')]
print(L)
L = ['目录/文件：' + d for d in os.listdir('/')]
print(L)
# 列表元素为二元组
L = [(source, dest) for source in list(range(1, 3)) for dest in list(range(11, 13))]
print(L)
# 列表生成式的可以使用多个变量
L = [{k, v} for k, v in {1: 'A', 2: 'B'}.items()]
print(L)

print("###### 生成器 ######")
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。