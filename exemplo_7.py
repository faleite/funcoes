""" Funções de ordem superior HOFs """

from typing import Any, Callable

soma_2 = lambda val: val + 2
#  In [2]: soma_2(2)
#  Out[2]: 4

#  In [3]: soma_2(soma_2(2))
#  Out[3]: 6

# Twice
def reaplica(func: Callable, val: Any) -> Any:
    """ Função que reaplica a função ao resultado da chamada. """
    return func(func(val))

#  In [5]: reaplica(soma_2, 0)
#  Out[5]: 4


def seleciona(op: str) -> Callable:
    """ Seleciona uma função, usando o seu nome. """
    ops = {
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y
    }
    return ops[op]

#  In [1]: seleciona('soma')
#  Out[1]: <function __main__.seleciona.<locals>.<lambda>(x, y)>

#  In [2]: seleciona('soma')(1,2)
#  Out[2]: 3

#  In [3]: seleciona('sub')(1,2)
#  Out[3]: -1

palavras = ['amar', 'transar', 'falar', 'abacaxi']

#  In [1]: sorted(palavras)
#  Out[1]: ['abacaxi', 'amar', 'falar', 'transar']

#  In [2]: sorted(palavras, key=lambda string: string[1])
#  Out[2]: ['falar', 'abacaxi', 'amar', 'transar']

#  In [3]: list(map(lambda val: val * 2, palavras))
#  Out[3]: ['amaramar', 'transartransar', 'falarfalar', 'abacaxiabacaxi']

#  In [4]: list(map(lambda val: val * 2, [1,2,3,4]))
#  Out[4]: [2, 4, 6, 8]

palavras = ['amar', 'transar', 'falar', 'abacaxi', 'xixi']

#  In [1]: from itertools import groupby

#  In [2]: groupby(palavras)
#  Out[2]: <itertools.groupby at 0x10e9d1f80>

#  In [3]: list(groupby(palavras, key=lambda string: string[-2:]))
#  Out[3]:
#  [('ar', <itertools._grouper at 0x10e8cbe20>),
 #  ('xi', <itertools._grouper at 0x10e601660>)]

#  In [4]:  list(filter(lambda x: x[-2:] == 'ar', palavras))
#  Out[4]: ['amar', 'transar', 'falar']


#  In [5]: from functools import reduce

#  In [6]: reduce(lambda x, y: x + y, [1,2,3,4,5])
#  Out[6]: 15

#  In [7]: reduce(lambda x, y: x * y, [1,2,3,4,5])
#  Out[7]: 120

#  In [8]: reduce(lambda x, y: x / y, [1,2,3,4,5])
#  Out[8]: 0.008333333333333333


#  In [9]: from itertools import takewhile

#  In [10]: list(takewhile(lambda x: x < 10, [8,9,10,11]))
#  Out[10]: [8, 9]

def take_cond(func, valores):
    for val in valores:
        if func(val):
            yield val
        else:
            break
