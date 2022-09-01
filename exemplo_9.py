""" Funções parciais (functools) """

from operator import add, itemgetter, mul
from functools import partial, reduce

# Métodos tradicionais ->
# Funçao que soma um numero x com 2:
#Opçao 1:
def soma_2(x):
    return x + 2
#Opçao 2:
soma_2 = lambda x: x + 2

# Métodos com operator -> add(a, b)
#Opçao 1:
def sum_2(x):
    return add(x, 2)
#Opçao 2:
sum_2 = lambda x: add(x, 2)

# Métodos com operator -> add(a, b)
#Opçao :
suma_2 = partial(add, 2)
#  In [3]: suma_2(20)
#  Out[3]: 22


reduce(add, [1, 2, 3, 4, 5]) # Somatório
reduce(mul, [1, 2, 3, 4, 5]) # Multiplicatório

somatorio = partial(reduce, add)
#  In [1]: somatorio([1,2,3,4])
#  Out[1]: 10

multiplicatorio = partial(reduce, mul)
#  In [3]: multiplicatorio([1,2,4,5])
#  Out[3]: 40

mul_2 = partial(mul, 2)
mul_2_all = partial(map, mul_2) # map -> itera em todos
#  In [1]: mul_2_all([1,2,3])
#  Out[1]: <map at 0x10cd3ee00>

#  In [2]: list(mul_2_all([1,2,3]))
#  Out[2]: [2, 4, 6]

ordernar_1 = partial(sorted, key=itemgetter(1))
#  In [1]: ordernar_1(['ab', 'ac', 'aa'])
#  Out[1]: ['aa', 'ab', 'ac']

def func(b, c, d, e, database=None):
    return database, b, c, d, e

func_postgres = partial(func, database='postgres')
func_maria = partial(func, database='mariaDB')
func_mongo = partial(func, database='mongoDB')

#  In [1]: func_postgres(1,2,3,4)
#  Out[1]: ('postgres', 1, 2, 3, 4)

#  In [2]: func_mongo(1,2,3,4)
#  Out[2]: ('mongoDB', 1, 2, 3, 4)

#  In [3]: func_mongo
#  Out[3]: functools.partial(<function func at 0x112326560>, database='mongoDB')

#  In [4]: hasattr(func_mongo, '__call__')
#  Out[4]: True
