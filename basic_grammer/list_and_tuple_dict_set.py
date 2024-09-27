"""
列表、元组、字典和集
"""
# list(Python内置的一种数据类型是列表：list。list是一种有序的集合)
print ('######list######')
classMates = ['a', 'b', 'c']
print(f'classMates:{classMates}')
print(f'len(classMates):{len(classMates)}')
print(f'classMates[0]:{classMates[0]}')
print(f'classMates[1]:{classMates[1]}')
print(f'classMates[2]:{classMates[2]}')
# index为-1就是最后一个元素
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

# tuple(另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改)
print ('######tuple######')
tuple1 = (1, 2, ['a', 'b'])
print(f'tuple={tuple1}')
print(f'tuple[0]:{tuple1[0]}')
print(f'tuple[1]:{tuple1[1]}')
print(f'tuple[2]:{tuple1[2]}')
print(f'tuple[-1]:{tuple1[-1]}')
print(f'tuple[2][0]:{tuple1[2][0]}')
print(f'tuple[2][1]:{tuple1[2][1]}')

print ('######dict######')
model_price_dict = {'4060': 2400, '4060Ti': 2800, '7700XT': 2900, '7800XT': 3400}
print(model_price_dict)
print(f'model_price_dict["7700XT"]: {model_price_dict['7700XT']}')
model_price_dict['4060Ti'] = 2850
print('model_price_dict["4060Ti"] = 2850')
print(f'model_price_dict["4060Ti"]: {model_price_dict['4060Ti']}')
print(f'key 4090Ti exist: {'4090Ti' in model_price_dict}')
print(f'key 7700XT exist: {'7700XT' in model_price_dict}')
print(f'model_price_dict.get(\'7700XT\'): {model_price_dict.get('7700XT')}')
print(model_price_dict.items())
print(model_price_dict.keys())
print(model_price_dict.values())
model_price_dict['4070Super'] = 5000
print('model_price_dict[\'4070Super\'] = 5000')
print(model_price_dict)
model_price_dict.pop('4070Super')
print('model_price_dict.pop(\'4070Super\')')
print(model_price_dict)
del model_price_dict['7800XT']
print('del model_price_dict[\'7800XT\']')
print(model_price_dict)
for key,value in model_price_dict.items():
    print(f'key:{key}, value:{value}')
print ('###########')
for key in model_price_dict:
    print(f'key:{key}, value:{model_price_dict[key]}')

print ('######set######')
print ('######set是无序和无重复元素的集合######')
set1 = {'a', 'b', 3, 'c'}
print(f'set1 = {set1}')
set1.add(4)
print(f'set1.add(4)')
print(set1)
set1.remove('a')
print('set1.remove(\'a\')')
print(set1)
set1.pop()
print('set1.pop()')
print(set1)
