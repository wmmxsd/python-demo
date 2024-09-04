"""
dict和set
"""
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