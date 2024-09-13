"""
设备模块
"""
from msilib.schema import Property


class Device(object):
    @Property
    def get_name(self):
        return self.__name

    @Property