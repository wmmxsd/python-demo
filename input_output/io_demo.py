"""
IO编程demo
"""

import logging
import os
import time
from io import StringIO, BytesIO
import shutil

logging.basicConfig(level=logging.DEBUG)

def read_file_1(filename):
    try:
        # with语句会自动管理资源的分配和释放，无需显式地在finally中调用close方法。
        with open(filename, 'r') as f:
            print(f.read())
    except IOError as e:
        print(f"Error reading file: {e}")

def read_file_2(filename):
    try:
        # with语句会自动管理资源的分配和释放，无需显式地在finally中调用close方法。
        with open(filename, 'r') as f:
            for line in f.readlines():
                print(line)
    except IOError as e:
        print(f"Error reading file: {e}")

def read_binary_file():
    try:
        with open('d411caef76094b3643c775d2e5cc7cd98c109df1.jpg', 'rb') as f:
            print(f.read())
    except IOError as e:
        print(f"Error reading file: {e}")

def read_gbk_file():
    try:
        with open('gbk-demo.txt', 'r', encoding='GBK', errors='strict') as f:
            print(f.read())
        with open('gbk-demo.txt', 'r', encoding='UTF-8', errors='ignore') as f:
            print(f.read())
    except IOError as e:
        print(f"Error reading file: {e}")

def write_gbk_file():
    try:
        with open('gbk-demo.txt', 'w', encoding='GBK', errors='strict') as f:
            # 覆盖写用w模式
            f.write('write_gbk_file()\n')
        with open('gbk-demo.txt', 'a', encoding='GBK', errors='strict') as f:
            # 追加用a模式
            f.write('write_gbk_file1()')
    except IOError as e:
        print(f"Error writing file: {e}")

def string_io_demo():
    str_io = StringIO()
    str_io.write('hello world from stringIO')
    try:
        with open('input-demo.txt', 'w', encoding='GBK', errors='strict') as f:
            # 覆盖写用w模式
            f.write(str_io.getvalue())
    except IOError as e:
        print(f"Error writing file: {e}")

def bytes_io_demo():
    bytes_io = BytesIO()
    bytes_io.write('hello world from BytesIO'.encode('GBK'))
    try:
        with open('input-demo.txt', 'w', encoding='GBK', errors='strict') as f:
            # 覆盖写用w模式
            f.write(bytes_io.getvalue().decode('GBK'))
    except IOError as e:
        print(f"Error writing file: {e}")

def os_demo():
    print(os.name)
    print(os.environ)
    print(os.environ.get('NUMBER_OF_PROCESSORS'))
    print(os.path.abspath(''))
    print(os.path.abspath('.'))
    print(os.path.abspath('./'))
    print(os.path.abspath('/'))

    print(os.path.relpath('.'))
    print(os.path.relpath('./'))
    print(os.path.relpath('/'))

    print(os.path.split('D:\\code\\github\\python-demo\\input_output\\gbk-demo.txt'))
    print(os.path.splitext('D:\\code\\github\\python-demo\\input_output\\gbk-demo.txt'))
    print(os.path.split('/Users/michael/testdir/file.txt'))
    print(os.path.splitext('/Users/michael/testdir/file.txt'))
    
    print([x for x in os.listdir(os.path.relpath('../basic_grammer'))
        if os.path.isfile(os.path.join(os.path.relpath('../basic_grammer'), x)) and os.path.splitext(x)[1] == '.py'])

    if not os.path.exists(os.path.join(os.path.abspath('./'), 'test1')):
        os.mkdir(os.path.join(os.path.abspath('./'), 'test1'))

    if not os.path.exists(os.path.relpath('test2')) and not os.path.exists(os.path.relpath('test3')):
        os.mkdir(os.path.relpath('test2'))
        os.mkdir( os.path.join(os.path.relpath('test2'), 'test2-1'))
        os.rename('test2', 'test3')

    os.rmdir(os.path.join(os.path.abspath('./'), 'test1'))
    os.rmdir(os.path.join(os.path.relpath('test3'), 'test2-1'))
    os.rmdir(os.path.relpath('test3'))

def shutil_demo():
    """
    shutil是os模块的补充，os模块没有提供创建文件、复制文件等函数
    """
    with open('shutil_demo.txt', 'w', encoding = 'utf-8') as f:
        f.write('shutil_demo.txt')
    shutil.copy('shutil_demo.txt', 'shutil_demo1.txt')
    shutil.copy2('shutil_demo1.txt', 'shutil_demo2.txt')
    shutil.move('shutil_demo2.txt', 'shutil_demo3.txt')
    print(os.path.abspath('/'), shutil.disk_usage(os.path.abspath('/')))

def dir_l_command():
    current_directory = os.getcwd()

    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        file_stats = os.stat(file_path)
        file_mode = oct(file_stats.st_mode)[-3:]
        file_size = file_stats.st_size
        file_time = time.ctime(file_stats.st_mtime)
        # 使用{:<X}和{:>X}占位符分别控制左对齐和右对齐，X是占位符宽度
        print(f"{file_mode:>3s} {file_size:<10d} {file_time:>20s} {file_name:<30s}")

# read_file_1('specialudisk-use.txt')
# read_file_2('specialudisk-use.txt')
# read_binary_file()
# read_gbk_file()
# write_gbk_file()
# string_io_demo()
# bytes_io_demo()
# os_demo()
shutil_demo()
# dir_l_command()