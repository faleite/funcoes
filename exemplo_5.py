""" Documentação de Funções
Relacionados:
- pycodestyle (lib para correção de code PEP - 257)
"""

from typing import NewType


Radiano = NewType('Radiano', int)

def calc_radianus_triangulo(x, y, H: list) -> Radiano:
    ...

def soma(x: int, y: int) -> int:
    # PEP - 257
    """ Soma dois tipos somáveis.

    :args:
        x: Objeto somável
        y: Objeto somável

    :returns: soma de dois somáveis.
    """
    ...

#  In [1]: soma.__doc__
#  Out[1]: ' Soma dois tipos somáveis.\n\n    :args:\n
#  x: Objeto somável\n        y: Objeto somável\n\n    :returns: soma de dois somáveis.\n    '
