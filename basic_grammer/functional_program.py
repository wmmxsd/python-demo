"""
函数式编程
允许把函数本身作为参数传入到另一个函数，同时函数的返回值也可以是函数
"""
# 只有函数名和既有函数名也有括号的区别
from functools import reduce


print('abs(-1):', abs(-1))
print('abs:', abs)
# 函数赋给变量
f = abs
print('f(-1):', f(-1))
print('f:', f)
# 函数当做参数
def abs_cus(x, f):
    return f(x)

print('abs_cus(-100, abs):', abs_cus(-100, abs))
# 函数当做返回值
def area_func(type, *parms):
    match type:
        case 0:
            return lambda: parms[0] * parms[1]
        case 1:
            return lambda: parms[0] * parms[0]

print(area_func(1, 1))
print(area_func(0, 3, 2)())

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum
print('lazy_sum(*range(1, 11)):', lazy_sum(*range(1, 11)))
print('lazy_sum(*range(1, 11))():', lazy_sum(*range(1, 11))())

# map/reduce/filter/sort
def multiply(x):
    return x * x
print('list(map(multiply, range(1, 11))):', list(map(multiply, range(1, 11))))

def fn(x, y):
    return x * 10 + y
print('reduce(sum, [1, 3, 5, 7, 0]):', reduce(fn, [1, 3, 5, 7, 0]))

def is_even(x):
    return x % 2 == 0
print('filter(is_even, range(1, 11))', list(filter(is_even, range(1, 11))))

print('sorted([1, 3, 90, -3.3, -20, 10])', sorted([1, 3, 90, -3.3, -20, 10]))
print('sorted([\'bob\', \'about\', \'Zoo\', \'Credit\'], key=str.lower)', sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print('sorted([\'bob\', \'about\', \'Zoo\', \'Credit\'], key=str.lower, reverse=True)', sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 测试1(首字母大写，其他小写):
def normalize(name):
    return name.capitalize() 
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 测试2(求积):
def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 测试(回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数):
def is_palindrome(n):
    n_str = str(n)
    if len(n_str) == 1:
        return True

    quot = len(n_str) // 2
    for index in range(0, quot + 1):
        if n_str[index] == n_str[len(n_str) - index - 1]:
            return True
        else:
            return False
  
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#测试
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
print('sorted(L, key = lambda t: t[0]):', sorted(L, key = lambda t: t[0]))
#按成绩从高到低排序
print('sorted(L, key = lambda t: t[0]):', sorted(L, key = lambda t: t[1], reverse = True))
