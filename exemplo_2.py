""" Paramêtros -> Argumentos pisicionais, e nomeados """

#1 Função Anonima -> Lambda
# *Função lambda não precisa receber nome
anonima = lambda param: param + 2
#  In [1]: anonima
#  Out[1]: <function __main__.<lambda>(param)> -> anonima é uma funçao que recebe um argumento
#  In [3]: anonima(2) # -> (2 = param) -> parametro
#  Out[3]: 4

anonima_plus = lambda param1, param2: param1 + param2
#  In [1]: anonima_plus
#  Out[1]: <function __main__.<lambda>(param1, param2)> -> recebe dois argumento
#  In [3]: anonima_plus(7, 7) # -> Faz a soma dos dois parametros (7 = param)
#  Out[3]: 14

# Função Nomeada:

#2 Argumentos posicionais
def soma_posicinal(x, y):
    """ X e Y são paramêtros posicionais. """
    return x + y
#  In [1]: soma(7, 7)
#  Out[1]: 14

#  In [1]: soma
#  Out[1]: <function __main__.soma(x, y)> # A função soma recebe dois parametros (x e y)

#3 Argumentos nomeados
def soma_nomeados(x=7, y=7):
    """
    X e Y são paramêtros nomeados.
    Parametro nomeados diz que ->
    -> na falta de X ou Y, valor 7 será usado.
    """
    print(f'x: {x}, y: {y}')
    return x + y

# Ilustração:
#  In [2]: soma_nomeados(1)
#  x: 1, y: 7
#  Out[2]: 8

#  In [3]: soma_nomeados(y=1)
#  x: 7, y: 1
#  Out[3]: 8

def soma_explicitamente_nomeados(*, x=7, y=7):
    """
    Ao incluir o * antes dos paramêtros X e Y
    X e Y tornão explicitamente nomeados
    Fazendo com que a função aceite apenas paramêtros explicitamente nomeados
    """
    print(f'x: {x}, y: {y}')
    return x + y

def soma_explicitamente_nomeados2(x=7, *, y=7):
    """
    Ao incluir o * antes do paramêtro Y
    Y torna-se explicitamente nomeado
    X não seja explicitamente nomeado
    """
    print(f'x: {x}, y: {y}')
    return x + y

#3
def soma_explicitamente_posicionais(x, y, /):
    """
    Ao incluir o / após os paramêtros X e Y
    A funçao passa a aceitar apenas argumentos posicionais
    """
    print(f'x: {x}, y: {y}')
    return x + y

#  In [10]: soma_explicitamente_posicionais(1, 2)
#  x: 1, y: 2
#  Out[10]: 3

def soma_tudo_mix(x, y, /, z, *, w):
    """
    Ao incluir o / após os paramêtros X e Y
    X e Y passa a ser argumentos estritamente posicionais
    Z passa ser misto
    Ao incluir o * antes do paramêtros W
    W passa a ser um paramêtro estritamente nomeado
    """
    print(f'x: {x}, y: {y}, z: {z}, w: {w}')
    return sum((x, y, z, w))

#  In [1]: soma_tudo_mix(1, 2, 3, w=1)
#  x: 1, y: 2, z: 3, w: 1
#  Out[1]: 7

#  In [2]: soma_tudo_mix(1, 2, z=3, w=1) # parametro Z é misto
#  x: 1, y: 2, z: 3, w: 1
#  Out[2]: 7
