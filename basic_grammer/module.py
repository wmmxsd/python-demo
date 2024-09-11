"""
模块demo
"""
# 引入其他模块
import sys


def test():
    # sys.argv用list存储了命令行的所有参数
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print(f'Hello, {args[1]}!')
    else:
        print('Too many arguments!')


# 作用域(在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。)
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
def _private_1():
    return '_private_1'


def _private_2():
    return '_private_2'


def greeting(name):
    if len(name) == 1:
        _private_1()
    else:
        _private_2()


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
if __name__ == '__main__':
    test()
else:
    print(f'{__name__} does\'t run test()')
