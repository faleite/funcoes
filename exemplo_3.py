""" Empacotamento e desempacotamento de argumentos """

#1 Empacotamento:
#  def my_sum(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    #  return sum((a, b, c, d, e, f, g, h, i, j, k, l, m, n, o))
def my_sum(*args): # *args -> Argumentos explicitamente posicionais
    """ Empacotamento """
    print(args)
    print(type(args))
    return sum(args)

#  In [1]: my_sum(1,2,3,4,5,6,7,8,9,1,2,3,47,1,2)
#  (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 47, 1, 2)
#  <class 'tuple'>
#  Out[1]: 101

def my_sum2(x, y, *args): # *args -> Argumentos explicitamente posicionais
    """ Empacotamento """
    print(args)
    print(type(args))
    print(x, y)
    return x, y, sum(args)

#  In [1]: my_sum2(1,2,3,4,5,6,7,8,9,1,2,3,47,1,2)
#  (3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 47, 1, 2)
#  <class 'tuple'>
#  1 2
#  Out[1]: (1, 2, 98)


#  def my_sum3(*args, **kwargs):
def my_sum3(*grupo_posicional, **grupo_nomeado):
    """ Empacotamento """
    print(grupo_posicional, grupo_nomeado)
    print(type(grupo_posicional), type(grupo_nomeado))
    return grupo_posicional, grupo_nomeado

#  In [2]: my_sum3(1,2,3,4,5, a=1, b=2)
#  (1, 2, 3, 4, 5) {'a': 1, 'b': 2}
#  <class 'tuple'> <class 'dict'>
#  Out[2]: ((1, 2, 3, 4, 5), {'a': 1, 'b': 2})


# Desempacotamento:
lista = [1, 2, 3, 4]

def meu_min(a, b, c, d):
    """ Desempacotamento """
    return min(a, b, c, d)

#  In [2]: meu_mim(1, 2, 3, 4)
#  Out[2]: 1

#  In [5]: meu_min(*lista)
#  Out[5]: 1

lista = [1, 2, 3, 4, 5]

def meu_min2(a, b, c, d, *args):
    """ Desempacotamento """
    return min(a, b, c, d, *args)

#  In [2]: meu_min2(*lista)
#  Out[2]: 1

#  In [4]: meu_min2(1,2,3,4,5,6,7, -1)
#  Out[4]: -1

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

def meu_max(a=0, b=0, c=0, d=0): # Paramentros nomeados
    """ Desempacotamento """
    return max((a, b, c, d))

#  In [2]: meu_max(**dicionario)
#  Out[2]: 4

#  In [1]: meu_max()
#  Out[1]: 0

l = [1, 2, 3]
d = {'d': 4, 'e': 5}

def meu_mix(a, b, c, d=0, e=0):
    """ Desempacotamento misto"""
    return a, b, c, d, e

#  In [1]: meu_mix(*l)
#  Out[1]: (1, 2, 3, 0, 0)

#  In [3]: meu_mix(*l, **d)
#  Out[3]: (1, 2, 3, 4, 5)
