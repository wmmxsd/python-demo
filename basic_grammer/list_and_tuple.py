"""
列表和元组
"""
#list(Python内置的一种数据类型是列表：list。list是一种有序的集合)
classMates = ['a', 'b', 'c']
print(f'classMates:{classMates}')
print(f'len(classMates):{len(classMates)}')
print(f'classMates[0]:{classMates[0]}')
print(f'classMates[1]:{classMates[1]}')
print(f'classMates[2]:{classMates[2]}')
#index为-1就是最后一个元素
print(f'classMates[-1]:{classMates[-1]}')
classMates.append('d')
print('classMates.append(\'d\')')
print(f'classMates:{classMates}')
print(f'classMates[-1]:{classMates[-1]}')
classMates.insert(1, '1')
print('classMates.insert(1, \'1\')')
print(f'classMates:{classMates}')
print(f'classMates[1]:{classMates[1]}')
print('classMates.pop()')
classMates.pop()
print(f'classMates:{classMates}')
print(f'classMates[-1]:{classMates[-1]}')
print('classMates.pop(-1)')
classMates.pop(-1)
print(f'classMates:{classMates}')
print(f'classMates[-1]:{classMates[-1]}')
classMates[1] = 'b'
classMates[2] = 'c'
print('classMates[1] = \'b\'')
print('classMates[2] = \'c\'')
print(f'classMates:{classMates}')
list1 = [1, 2, 'a', [3, 4]]
print(f'list1:{list1}')
print(f'len(list1):{len(list1)}')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(f'L:{L}')
print(f'Apple:{L[0][0]}')
print(f'Python:{L[1][1]}')
print(f'Bob:{L[2][2]}')
print ('###########')
#tuple(另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改)
tuple1 = (1, 2, ['a', 'b'])
print(f'tuple={tuple1}')
print(f'tuple[0]:{tuple1[0]}')
print(f'tuple[1]:{tuple1[1]}')
print(f'tuple[2]:{tuple1[2]}')
print(f'tuple[-1]:{tuple1[-1]}')
print(f'tuple[2][0]:{tuple1[2][0]}')
print(f'tuple[2][1]:{tuple1[2][1]}')
print ('###########')
