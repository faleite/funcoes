""" Anotações de tipo de argumentos

Para pesquisar:
- PEP-484
- mypy
- monkeytype
"""

# Anotações de tipo é usada quando preciso especificar
# o tipo que a variável ou função deve retornar ou aceitar

from numbers import Number
from typing import Union, Any, List, Dict, Sequence, Text

def soma(x: int, y: int) -> int: # X e Y espera um numero inteiro, A função espera n int
    return x + y

# Number = int, float e complex
Somavel = Union[Number, str, list]

def soma2(x: Somavel, y: Somavel) -> Somavel:
    return x + y


def identidade(val: Any) -> Any:
    return val

def meu_sum(l: List[Number]) -> Number:
    return sum(l)

#  In [2]: meu_sum([1,2,3])
#  Out[2]: 6

def cadastro_usuario(
    nome: str,
    idade: int,
    gostos: List[str]
) -> Dict[str, Union[str, int, List[str]]]:
    return {
        'nome': nome,
        'idade': idade,
        'gostos': gostos
    }

#  In [2]: cadastro_usuario
#  Out[2]: <function __main__.cadastro_usuario(
#  nome: str, idade: int, gostos: List[str]) -> Dict[str, Union[str, int, List[str]]]>

#  In [3]: cadastro_usuario('Fabricio', 37, ['Python', 'Música'])
#  Out[3]: {'nome': 'Fabricio', 'idade': 37, 'gostos': ['Python', 'Música']}

def meu_min(seq: Sequence):
    return min(seq)


def converte_para_reais(valor: Text):
    ...
