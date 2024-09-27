class Chain(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, item):
        """
        只有在没有找到属性的情况下，才调用__getattr__
        """
        if not isinstance(item, str):
            raise AttributeError()
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        """
        类似于java的toString()方法
        """
        return self._path

    def __call__(self):
        """
        直接对实例进行调用。调用方式：instance()
        """
        return self._path


    __repr__ = __str__

print(Chain().status.user.timeline.list)
c = Chain("all")
print(c())