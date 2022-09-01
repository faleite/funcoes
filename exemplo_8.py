""" Módulo Operator """

from operator import (
    add, itemgetter, mul, sub
)
from functools import reduce

#  In [1]: add(1,1)
#  Out[1]: 2

# Operator -> operações ex. "1 de operação com 1":
#  1 <op> 1:
#  1 + 1
#  1 - 1
#  1 / 1
#  1 // 1
#  1 * 1

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x - y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
#  >>> 15
#  >>> -13
#  >>> 120

print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(sub, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))
#  >>> 15
#  >>> -13
#  >>> 120

palavras = ['amar', 'transar', 'falar', 'abacaxi', 'xixi']

sorted(palavras, key=lambda string: string[1])
#  Out[1]: ['falar', 'abacaxi', 'xixi', 'amar', 'transar']

sorted(palavras, key=itemgetter(1))
#  Out[1]: ['falar', 'abacaxi', 'xixi', 'amar', 'transar']
sorted(palavras, key=itemgetter(-1))
#  Out[2]: ['abacaxi', 'xixi', 'amar', 'transar', 'falar']
