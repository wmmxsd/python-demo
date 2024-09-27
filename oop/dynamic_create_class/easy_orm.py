"""
字段类
"""


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        # <Field:ip>
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        # Python 2 中调用父类构造函数的常见方式
        # super(StringField, self).__init__(name, 'varchar(100)')
        # Python 3 中的super函数会自动根据方法解析顺序找到正确的父类方法进行调用
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        # Python 2 中调用父类构造函数的常见方式
        # super(IntegerField, self).__init__(name, 'bigint')
        # Python 3 中的super函数会自动根据方法解析顺序找到正确的父类方法进行调用
        super().__init__(name, 'bigint')


# 元类，用于在创建模型类（如User类）时进行一些特定的处理
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
# 如果没有找到，就继续在父类Model中查找metaclass，
# 找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
