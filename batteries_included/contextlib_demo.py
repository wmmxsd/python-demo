"""
上下文管理，类实现了上下文管理就能使用with关键字来自动关闭资源
"""
from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query(object):
    """
    Query类，执行查询sql
    实现上下文管理是通过__enter__和__exit__这两个方法实现的
    """
    def __init__(self, sql):
        self.sql = sql

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('end')

    def query(self):
        print('exec %s' % self.sql)

with Query('select * from table') as q:
    q.query()

class Update(object):
    def __init__(self, sql, params):
        self.sql = sql
        self.params = params

    def update(self):
        print('exec %s %s' % (self.sql, self.params))
        return 1

# @contextmanager比__enter__和__exit__更简洁的实现上下文管理
@contextmanager
def create_update(sql, params):
    print('begin')
    update = Update(sql, params)
    yield update
    print('end')

with create_update('update from table set name = ? where id = ?', ['tom', 1]) as u:
    u.update()

# 函数执行前后自动执行特定代码也可以使用@contextmanager，类似于切面（公共模块和业务代码分离）
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)

with tag('h1'):
    print('PYTHON')

# closing()可以直接把一个对象变成拥有上下文的对象
with closing(urlopen('https://www.baidu.com/')) as response:
    for line in response:
        print(line)


