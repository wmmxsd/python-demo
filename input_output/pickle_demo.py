"""
序列化demo
"""

import pickle
import json

from oop.device import Device

d = dict(name = '张三', age = 22, score = 99)
# 序列化成二进制
print('pickle.dumps(d):', pickle.dumps(d))

# 序列化成二进制并且存储到硬盘
try:
    with open('d.txt', 'wb') as f:
        pickle.dump(d, f)
except IOError as e:
    print(f'Error pickling: {e}')

# 文件反序列化对象
try:
    with open('d.txt', 'rb') as f:
        d_copy = pickle.load(f)
        print('d_copy:', d_copy)
except IOError as e:
    print(f'Error unpickling: {e}')

# 序列化成json
print('json.dumps(d):', json.dumps(d))
print('json.dumps(d, ensure_ascii = False):', json.dumps(d, ensure_ascii = False))
json_str = '{"name": "bob", "age": 22, "score": 99}'
print('json.loads(json_str):', json.loads(json_str))

# 序列化自定义对象
d = Device()
d.set_ip(chr(50))
d.score = 99
# __dict__属性
print('json.dumps(d, default = lambda obj: obj.__dict__)', json.dumps(d, default = lambda obj: obj.__dict__))
print('json.dumps(d, default = lambda obj: obj.to_dict()):', json.dumps(d, default = lambda obj: obj.to_dict()))

d_json_str = '{"ip": "2", "score": 99}'
print('json.loads(d_json_str, object_hook = Device.to_device):', json.loads(d_json_str, object_hook = Device.to_device))

