"""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。先定义metaclass，然后创建类。
简单演示
"""


class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        # 准备创建的类的对象；类的名字；类继承的父类集合；类的方法集合。
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


list_0 = list()
list_1 = MyList()
# AttributeError: 'list' object has no attribute 'add'
# list_0.add(1)
list_1.add(1)
print(list_0)
print(list_1)

