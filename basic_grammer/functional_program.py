"""
函数式编程
允许把函数本身作为参数传入到另一个函数，同时函数的返回值也可以是函数
"""
from functools import reduce
import functools
import time

# 只有函数名和既有函数名也有括号的区别
print('abs(-1):', abs(-1))
print('abs:', abs)

# 函数赋给变量(跟js的函数赋给变量一样)
f = abs
print('f(-1):', f(-1))
print('f:', f)

# 函数当做参数
def abs_cus(x, f):
    return f(x)

print('abs_cus(-100, abs):', abs_cus(-100, abs))

# 函数当做返回值(函数被返回时不会执行该函数，只有再次调用该函数时才会执行)
def area_func(type, *parms):
    match type:
        case 0:
            return lambda: parms[0] * parms[1]
        case 1:
            return lambda: parms[0] * parms[0]

print(area_func(1, 1))
print(area_func(0, 3, 2)())

def lazy_sum(*args):
    ax = 0
    def sum():
        for x in args:
            # 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
            nonlocal ax
            ax = ax + x
        return ax
    return sum

print('lazy_sum(*range(1, 11)):', lazy_sum(*range(1, 11)))
print('lazy_sum(*range(1, 11))():', lazy_sum(*range(1, 11))())

# 匿名函数（没有def关键字和函数名的函数）
lambda x: x * x

def multify(x):
    return x * x
# 上面的两个函数分别是匿名函数和普通函数，作用一样，匿名函数需要lambda关键字，只能有一个表达式，不需要写return关键字。

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

# 装饰器（类似于java的装饰模式）
def log(func):
    # *args, **kw的写法可以让wrapper函数接受任意参数的调用
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        before = time.time()
        func(*args, **kw)
        after = time.time()
        print('call %s() takes %f' % (func.__name__, after - before))
    return wrapper

@log
def now():
    print('8888-88-88')
    
now()

def log_with_text(*text):
    def decorator(func):
        # 将wrapper函数的_name_属性改为参数func的_name_
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for t in text:
                print(f'{t}')
            return func(*args, **kw)
        return wrapper
    return decorator

@log_with_text('execute')
def now1():
    print('8888-88-88')
    
now1()

# 偏函数（无须自己定义函数，直接使用functools.partial函数来创建一个函数,这个新函数可以固定住原函数的部分参数，从而在调用时更简单。）
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

# 自定义10进制转为2进制函数
def int_to_2(x):
    return int(x, 2)

int_to_2_partial = functools.partial(int, base = 2)

print('int_to_2(1000000):', int_to_2('1000000'), ';int_to_2_partial(1000000):', int_to_2_partial('1000000'))

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

# 测试3(回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数):
def is_palindrome(n):
    n_str = str(n)
    if len(n_str) == 1:
        return True

    quot = len(n_str) // 2
    for index in range(0, quot + 1):
        if n_str[index] == n_str[len(n_str) - index - 1]:
            return True
        return False

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#测试4(排序)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
print('sorted(L, key = lambda t: t[0]):', sorted(L, key = lambda t: t[0]))
#按成绩从高到低排序
print('sorted(L, key = lambda t: t[0]):', sorted(L, key = lambda t: t[1], reverse = True))

# 测试5(利用闭包返回一个计数器函数，每次调用它返回递增整数):
def createCounter():
    sum = 0
    def counter():
        nonlocal sum
        sum = sum + 1
        return sum
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 测试6(请用匿名函数改造下面的代码）:
def is_odd(n):
    return n % 2 == 1
print('list(filter(is_odd, range(1, 20)))', list(filter(is_odd, range(1, 20))))
print('list(filter(lambda n: n % 2 == 1, range(1, 20)))', list(filter(lambda n: n % 2 == 1, range(1, 20))))

# 测试7（请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间）：
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
