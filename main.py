from itertools import *

s = 'yut'
for x in product(s, repeat=6):
    a = ''.join(x)
    print(a)
