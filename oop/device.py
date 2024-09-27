"""
设备模块
"""


class Device(object):
    def __init__(self):
        self._score = None
        self.ip = None

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        if not isinstance(ip, str):
            raise ValueError("ip must be an str")
        if ord(ip) < 0 or ord(ip) > 100:
            raise ValueError("ip's ord must be between 0 and 100")
        self.ip = ip

    # @property 装饰器提供了一种更简洁的方式来定义属性的访问和修改。
    # 它允许你像访问普通属性一样访问计算属性或进行属性的验证，而不需要显式地调用方法。
    # 例如，obj.attribute 而不是 obj.get_attribute()。
    @property
    def score(self):
        # 变量前面加一个下划线通常是一个实例变量，它表示对象的一个属性值，但在命名上带有一个下划线前缀，按照 Python 的命名约定，这暗示这个变量是 “受保护的”，
        # 即虽然可以直接访问，但开发人员应该谨慎地直接操作它，最好通过属性的 getter 和 setter 方法来访问和修改它
        return self._score

    # 必须保证@后面的名称必须和@property装饰器修饰的函数名及下面这个函数名保持一致
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer")
        if score < 0 or score > 100:
            raise ValueError("score must be between 0 and 100")
        self._score = score

device = Device()
# 使用@property访问或者设置属性时更简洁。
device.set_ip(chr(50))
print('device.get_ip():', device.get_ip())
device.score = 88
print('device.score:', device.score)

