""" Funções como objeto de primeira classe. """

from typing import Callable, Dict
from numbers import Number

#1
func = lambda: 'resultado da função'


calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x/ y
}
#  In [1]: calc
#  Out[1]:
#  {'soma': <function __main__.<lambda>(x, y)>,
#  'sub': <function __main__.<lambda>(x, y)>,
#  'mult': <function __main__.<lambda>(x, y)>,
#  'div': <function __main__.<lambda>(x, y)>}

#  In [2]: calc['soma']
#  Out[2]: <function __main__.<lambda>(x, y)>

#  In [3]: calc['soma'](1,1)
#  Out[3]: 2

#  In [4]: calc['sub'](1,1)
#  Out[4]: 0

#  In [5]: calc['mult'](1,1)
#  Out[5]: 1

#  In [6]: calc['div'](1,1)
#  Out[6]: 1.0

def soma(x: Number, y: Number) -> Number:
    """ Soma dois números. """
    return x + y

def sub(x: Number, y: Number) -> Number:
    """ Subtrai dois números. """
    return x - y


def mult(x: Number, y: Number) -> Number:
    """ Multiplica dois números. """
    return x * y

def div(x: Number, y: Number) -> Number:
    """ Dividi dois números. """
    return x / y

calc_nomeado = {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div
}

#  In [1]: calc_nomeado
#  Out[1]:
#  {'soma': <function __main__.soma(x: numbers.Number, y: numbers.Number) -> numbers.Number>,
 #  'sub': <function __main__.sub(x: numbers.Number, y: numbers.Number) -> numbers.Number>,
 #  'mult': <function __main__.mult(x: numbers.Number, y: numbers.Number) -> numbers.Number>,
 #  'div': <function __main__.div(x: numbers.Number, y: numbers.Number) -> numbers.Number>}

#  In [2]: calc_nomeado['soma'](1,1)
#  Out[2]: 2


somas = [
    lambda x: x + 0,
    lambda x: x + 1,
    lambda x: x + 2
]

#  In [1]: somas
#  Out[1]:
#  [<function __main__.<lambda>(x)>,
 #  <function __main__.<lambda>(x)>,
 #  <function __main__.<lambda>(x)>]

#  In [2]: somas[2](1)
#  Out[2]: 3


def soma_1(x: Number) -> Number:
    """ Soma 1 a qualquer x de entrada. """
    return x + 1

#  In [1]: soma_1(1)
#  Out[1]: 2

#  In [2]: (soma_1,)[0](1) # (soma_1,) -> caracteriza uma tupla.
#  Out[2]: 2
