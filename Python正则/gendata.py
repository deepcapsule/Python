"""
用于正则表达式练习的数据生成器
"""

from random import randrange, choice
from string import ascii_lowercase as lc
# from sys import maxsize
from time import ctime

MAXSIZE = 2**32
tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(MAXSIZE)    # pick date
    dtstr = ctime(dtint)          # date string
    llen = randrange(4, 8)        # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)    # domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom,
                                      choice(tlds), dtint, llen, dlen))
