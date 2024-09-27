from enum import Enum, UNIQUE, unique

MONTH = Enum('MONTH', (('JAN', 1), ('FEB', 2)))
print(MONTH.FEB)
print(MONTH.FEB.name)
print(MONTH.FEB.value)

for name, member in MONTH.__members__.items():
    print(f'name => {name}, value => {member.value}')


@unique
class WEEKEND(Enum):
    SUN = ('星期天', 0)
    MON = ('星期一', 1)
    TUE = ('星期二', 2)
    WED = ('星期三', 3)
    THU = ('星期四', 4)
    FRI = ('星期五', 5)
    SAT = ('星期六', 6)


print(WEEKEND.MON)
print(WEEKEND['TUE'])
print(WEEKEND.WED.name)
print(WEEKEND.THU.value)
print(WEEKEND.FRI.value[0])
print(WEEKEND.SAT.value[1])

for name, member in WEEKEND.__members__.items():
    print(f'name => {name}, chinese name => {member.value[0]}, index => {member.value[1]})')

class SEX(Enum):
    MALE = 0
    FEMALE = 1

class User(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

george = User('George', SEX.MALE)
print('george.sex == SEX.MALE', george.sex == SEX.MALE)