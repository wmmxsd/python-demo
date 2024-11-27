"""
迭代
"""

import itertools


def count():
    for x in itertools.count(10000, 100000):
        print(x)


def cycle():
    for y in itertools.cycle('ABC'):
        print(y)

def repeat():
    for x in itertools.repeat('ABC', 10):
        print(x)

def chain():
    for x in itertools.chain('ABC', range(10)):
        print(x)

# count()
# cycle()
repeat()
chain()



