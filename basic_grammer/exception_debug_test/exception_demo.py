"""
异常处理
"""
import logging
from functools import reduce


def except_exec_order_demo1():
    """
    异常执行顺序测试1
    """
    print('except_demo1 START')
    try:
        print('try start')
        10 / 0
        print('try end')
    except ValueError as e:
        print('except:', e)
    except ZeroDivisionError as e:
        print('except:', e)
    print('except_demo1 END')


def except_exec_order_demo2():
    """
    异常执行顺序测试2
    """
    print('except_demo2 START')
    try:
        print('try start')
        10 / 0
        print('try end')
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        # 不管报错与否最终都会执行
        print('finally')
    print('except_demo2 END')


def second_level(s):
    return 10 / s


def first_level(s):
    return second_level(s) * 2


# 多级捕获异常
def multi_level_call(s):
    """
    使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用。只需要主方法进行异常捕获即可
    """
    try:
        first_level(s)
    except Exception as e:
        print('multi_level_call except:', e)
        # Python内置的logging模块可以非常容易地记录错误信息并且程序能够继续运行
        # logging.exception(e)
    print('multi_level_call END')


class CustomError(Exception):
    pass


def throw_except_demo(s):
    """
    异常抛出
    """
    if s > 100:
        raise CustomError('invalid value: %s' % s)
    return s

# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
def str2num(s):
    # return int(s)
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
        logging.exception(e)

except_exec_order_demo1()
except_exec_order_demo2()
multi_level_call(0)
throw_except_demo(200)
main()
