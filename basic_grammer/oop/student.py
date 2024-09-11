# class关键字定义类，类名首字母大写，小括号中写上父类，如果没有合适的父类就用object类
import types


class Student(object):
    # 类属性
    school = 'Primary school'


    # __init__方法是类创建实例时的初始化方法，其第一个参数永远是self，表示实例本身，创建实例是self参数无须填写，python解释器会自动添加进来
    def __init__(self, name, score):
        self.name = name
        # 字段前面加上__后外部无法访问
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print(self.name, self.__score)

    def print_school(self):
        print('self.school', self.school)
        print('Student.school', Student.school)
        self.school = 'High School'
        print('self.school = \'High School\'')
        print('self.school', self.school)
        print('Student.school', Student.school)
        del self.school
        print('del self.school')
        print('self.school', self.school)
        print('Student.school', Student.school)

    # type()函数和isinstance()函数使用
    def print_info(self):
        """
        输出对象信息(type()、isinstance()、dir()函数、对象内置属性和方法)
        """
        # 判断对象类型可以使用type()函数
        print('######type()######')
        print('type(1) == int ', type(1) == int)
        print('type(\'a\') == str ', type('a') == str)
        print('type(abs) == types.BuiltinFunctionType ', type(abs) == types.BuiltinFunctionType)
        print('type(abs) == types.BuiltinMethodType ', type(abs) == types.BuiltinMethodType)
        print('type(abs) == types.FunctionType ', type(abs) == types.FunctionType)
        print('type(Student) == types.ModuleType ', type(Student) == types.ModuleType)
        print('type(Student.print_type) == types.FunctionType ', type(Student.print_info) == types.FunctionType)
        print('type(Student.print_type) == types.MethodType ', type(Student.print_info) == types.MethodType)
        print('type(Student(\'1\', 22)) == types.ModuleType ', type(Student('1', 22)) == types.ModuleType)
        print('type(None) == types.NoneType ', type(None) == types.NoneType)

        print('\n######isinstance()######')
        #能用type()函数可以用instance()函数代替，instance()函数不仅可以判断对象类型，还可以判断class类型
        print('isinstance(Student, types.ModuleType)', isinstance(Student('1', 1), Student))
        print('isinstance([1, 2, 3, 4 ,5], (list, tuple))', isinstance([1, 2, 3, 4 ,5], (list, tuple)))

        print('\n######dir()######')
        print('dir(\'ABC\')', dir('ABC'))
        print('dir(Student)', dir(Student))

        if hasattr(self, 'name'):
            print('getattr(self, \'name\')', getattr(self, 'name'))
        else:
            print('no name')

        if hasattr(self, '__score'):
            print('getattr(self, \'__score\')', getattr(self, '__score'))
        else:
            print('no __score')

        if hasattr(self, 'score'):
            print('getattr(self, \'score\')', getattr(self, 'score'))
        else:
            print('no score')

        if hasattr(self, 'sex'):
            print('getattr(self, \'sex\')', getattr(self, 'sex'))
        else:
            print('no sex, create now')
            setattr(self, 'sex', '男')
            print('getattr(self, \'sex\')', getattr(self, 'sex'))

        if hasattr(self, 'print_info'):
            print('getattr(self, \'print_info\')', getattr(self, 'print_info'))
        else:
            print('no print_info')


        if hasattr(self, 'set_score'):
            set_score_attr = getattr(self, 'set_score')
            print('getattr(self, \'set_score\')', set_score_attr)
            set_score_attr(22)
            print(self.__score)
        else:
            print('no set_score')

