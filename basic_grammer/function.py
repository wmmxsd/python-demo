"""
函数使用
"""
import math

print("######内置函数######")
print(f'abs(-10.1):{abs(-10.1)}')
print(f'max(-10.1, 1, 1.1, 0):{max(-10.1, 1, 1.1, 0)}')
print(f'min(-10.1, 1, 1.1, 0):{min(-10.1, 1, 1.1, 0)}')
print(f'int(\'123\'):{int('123')}')
print(f'float(\'123.123\'):{float('123.123')}')
print(f'str(\'123.123\'):{str('123.123')}')
print(f'bool(0):{bool(0)};bool(1):{bool(1)};bool(111):{bool(111)}')
print(f'bin(16):{bin(16)}')
print(f'hex(16):{hex(16)}')
print(f'bytes(16):{bytes(16)}')

print("######自定义函数######")
def my_abs(num):
    if not isinstance(num, (int, float)):
        raise TypeError('请输入数字')
    return abs(num)

print(f'my_abs(-1):{my_abs(-1)}')
# print(f'my_abs(s):{my_abs('s')}')

def nop():
    """ 空函数 """
    pass

print(f'nop():{nop()}')

def move(x, y, step, angle = 0):
    """ 返回多个值 """
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100, 100, 60, math.pi / 6)
print(x, y)

print("######默认参数######")
def param(sort_name, sort_order = 'asc', page_number = 1, page_size = 10):
    """
    <p>默认参数demo</p>
    <p>返回排序和截取sql</p>
    """
    return f'order by {sort_name} {sort_order} limit {(page_number - 1) * page_size} {page_number * page_size}'

print(param('ip'))
print(param('ip', 'desc'))
print(param('ip', 'desc', 10))
print(param('ip', 'desc', 10, 20))
print(param('ip', page_size = 30))

print("######可变参数######")
def cal_list(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

num_list = [1, 2 ,3]
print(cal_list(num_list))

def cal_variable(*numbers):
    """
    可变参数和列表参数比较起来，调用时的参数写法更加简洁
    """
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(cal_variable(1, 2, 3))
# 函数的参数为可变参数时，如果传入列表类型参数，可直接在参数名前加一个*号
print(cal_variable(*num_list))

print("######关键字参数######")
def add_user(name, role_id, org_id, **other):
    if 'mail' in other:
        pass
    if 'phone' in other:
        pass
    print(f'name:{name}, role_id:{role_id}, org_id:{org_id}, other:{other}')

add_user('oper', 'oper', 'tokyo')
add_user('oper', 'oper', 'tokyo', mail = '1@1.com', phone = '111', remark = 'main')
user_info = {'mail' :'1@1.com', 'phone' : '111', 'remark' :  'main'}
add_user('oper', 'oper', 'tokyo', **user_info)

# 关键字参数命名
def add_user_name1(name, role_id, org_id, *, mail, phone = '-', remark):
    print(f'name:{name}, role_id:{role_id}, org_id:{org_id}, mail:{mail}, phone:{phone}, remark:{remark}')

add_user_name1('oper', 'oper', 'tokyo', mail = '1@1.com', remark = '9')

# 可变参数+关键字参数命名(后面的命名关键字参数无需加*号)
def add_user_name2(name, role_id, org_id, *args, mail, phone = '-', remark):
    print(f'name:{name}, role_id:{role_id}, org_id:{org_id}, mail:{mail}, phone:{phone}, remark:{remark}, args:{args}')

add_user_name2('oper', 'oper', 'tokyo', 'args1', 'args2', 'args3', mail = '1@1.com', remark = '9')
args = ['args1', 'args2', 'args3']
add_user_name2('oper', 'oper', 'tokyo', *args, mail = '1@1.com', remark = '9') 

print("######复合参数######")
#在python中，函数的参数可以包含使用普通参数、带默认值的参数、可变参数、关键字参数和命名关键字参数
#但是参数必须按照：普通参数、带默认值的参数、可变参数、关键字参数、命名关键字参数的顺序来定义。
#虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
def complex_parameter_func(ordin, default = 'default', *variable, key_word_with_name1 = 'key_word_with_name1', key_word_with_name2, **key_word):
    print(f'orgin:{ordin}, default:{default}, variable:{variable}, key_word_with_name1:{key_word_with_name1}, key_word_with_name2:{key_word_with_name2}, key_word:{key_word}')

complex_parameter_func('普通参数', key_word_with_name2 = 'key_word_with_name2')
complex_parameter_func('普通参数', 'd', *args, key_word_with_name2 = 'key_word_with_name2', **user_info)

def mul(*eles):
    if len(eles) == 0:
        raise TypeError('参数为空')
    product = 1
    for ele in eles:
        product = product * ele
    return product

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')
        
#递归
def fact1(n):
    """
    n!=1*2*3*...*(n-1)*n=(n-1)!*n
    """
    if n == 1:
        return 1
    return n * fact1(n - 1)

print(fact1(5))
# print(fact1(1000))

def fact2(n, product):
    """
    n!=1*2*3*...*(n-1)*n=(n-1)!*n
    """
    if n == 1:
        return product
    return fact2(n - 1, product * n)

print(fact2(5, 1))

def tower_of_hanoi(disk_num):
    if disk_num == 0:
        return 0
    return 2 * tower_of_hanoi(disk_num - 1) + 1
print(tower_of_hanoi(1))
print(tower_of_hanoi(2))
print(tower_of_hanoi(3))
print(tower_of_hanoi(4))
