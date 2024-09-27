from basic_grammer.oop.student import Student

print('student.py')
tom = Student('tom', 99)
jerry = Student(name = 'jerry', score = 99)

print('tom.name:', tom.name)
tom.print_score()
jerry.print_score()
tom.age = 22
print('tom.age:', tom.age)

def add_score(self, score):
    self.set_score(self.get_score() + score)

# 给类和实例动态绑定属性和函数
Student.add_score = add_score

tom.add_score(10)
print('tom.get_score():', tom.get_score())
jerry.add_score(10)
print('jerry.get_score():', jerry.get_score())

# AttributeError: 'Student' object has no attribute 'age'
# print('jerry.age:', jerry.age)
print('tom.get_score():', tom.get_score())
tom.print_info()
tom.print_school()

print(tom)







