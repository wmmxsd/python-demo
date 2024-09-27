from basic_grammer.oop.extend_and_polymorphic.extend_and_polymorphic import Animal, Dog, Cat, ToyCar

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