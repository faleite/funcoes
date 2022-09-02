""" Funções aninhadas.
- Funções dentro de Funções
"""

from difflib import ndiff
from typing import List, NoReturn

# Ex de função dentro de função
def func():
    #função func_ só fuciona ao chamar a função principal
    def func_():
        ...
    ...

#  def file_diff(file_1: str, file_2: str):
#      content_1 = open(file_1).readlines()[1:-1]
#      content_2 = open(file_2).readlines()[1:-1]

    #  print(''.join(ndiff(content_1, content_2)))

#  In [3]: file_diff('texto_1.txt', 'texto_2.txt')
#  - oi
#  + ola
  #  meu
  #  nome
  #  é
#  - Goku
#  + Fabricio


def file_diff(file_1: str, file_2: str) -> NoReturn:

    def read_file(file: str) -> List:
        """ Abre o arquivo, ignorando a linha final e inicial. """
        return [
            e.replace(',', '')
            for e in open(file).readlines()[1:-1]
        ]

    content_1 = read_file(file_1)
    content_2 = read_file(file_2)

    print(''.join(ndiff(content_1, content_2)))

#  In [3]: file_diff('texto_1.txt', 'texto_2.txt')
#  - oi
#  + ola
  #  meu
  #  nome
  #  é
#  - Goku
#  + Fabricio
