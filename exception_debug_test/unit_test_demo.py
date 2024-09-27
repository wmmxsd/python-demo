import unittest

from oop.chain import Chain


class StudentTest(unittest.TestCase):
    # 在每调用一个测试方法前被执行
    def setUp(self):
        print('setUp')

    # 在每调用一个测试方法后被执行
    def tearDown(self):
        print('tearDown')

    def test_init(self):
        chain = Chain('')
        self.assertEqual(chain._path, '')

    def test_getattr(self):
        chain = Chain()
        self.assertEqual(chain.__getattr__('usr').__str__(), '/usr')

    def test_getattr_error(self):
        chain = Chain()
        with self.assertRaises(AttributeError):
            chain.__getattr__([1, 2, 3])


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError('invalid score')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


# 一旦编写好单元测试，我们就可以运行单元测试。
# 最简单的运行方式是在mydict_test.py的最后加上两行代码
# 这样就可以把mydict_test.py当做正常的python脚本运行
# python StudentTest.py
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试，可以一次批量运行很多单元测试
if __name__ == '__main__':
    unittest.main()
