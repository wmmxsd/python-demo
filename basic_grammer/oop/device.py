"""
设备模块
"""


class Device(object):
    def __init__(self, ip, score):
        self.ip = ip
        # 变量前面加一个下划线通常是一个实例变量，它表示对象的一个属性值，但在命名上带有一个下划线前缀，按照 Python 的命名约定，这暗示这个变量是 “受保护的”，
        # 即虽然可以直接访问，但开发人员应该谨慎地直接操作它，最好通过属性的 getter 和 setter 方法来访问和修改它
        self._score = score

    @property
    def score(self):
        return self._score

    # 必须保证@后面的名称必须和@property装饰器修饰的函数名及下面这个函数名保持一致
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer")
        if score < 0 or score > 100:
            raise ValueError("score must be between 0 and 100")
        self._score = score
