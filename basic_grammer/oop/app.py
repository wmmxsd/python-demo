import student
from basic_grammer.oop.extend_and_polymorphic import Animal, Dog, Cat, ToyCar

print('student.py')
tom = student.Student('tom', 99)
jerry = student.Student(name='jerry', score=99)

print('tom.name:', tom.name)
tom.print_score()
jerry.print_score()
tom.age = 22
print('tom.age:', tom.age)
# AttributeError: 'Student' object has no attribute 'age'
# print('jerry.age:', jerry.age)
print('tom.get_score():', tom.get_score())
tom.print_info()
tom.print_school()

print('\nextend_and_polymorphic.py')
def run(animal):
    animal.run()

print('isinstance(Animal(), Animal) ', isinstance(Animal(), Animal))
print('isinstance(Dog(), Animal)', isinstance(Dog(), Animal))
print('isinstance(Animal(), Cat) ', isinstance(Animal(), Cat))

run(Animal())
run(Dog())
run(Cat())
run(ToyCar())