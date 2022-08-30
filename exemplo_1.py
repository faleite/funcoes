""" Tipos de Funções em Python """

#1 Maneira tradicional de chmar uma função
# Função Nomeada
def funcao_nomeada():
    return 'Oi'
# Para chamar a função "minha_funcao" eu uso o abre e fecha parenteses
# após seu nome -> () -> Call
# >>> funcao_nomeada()
# >>> 'Oi'

#2 Função Anonima -> Lambda
# Função lambda não precisa receber nome
anonima = lambda : 'Oi'
# Para chamar a função "anonima" eu uso o abre e fecha parenteses
# após seu nome -> () -> Call
# >>> anonima()
# >>> 'Oi'

#3 Outra manira de fazer uma função em python é usando Classes
# Classe que se comporta como uma função
class FuncaoClasse:
    def __call__(self):
        return 'Oi'
#  >>> FuncaoClasse()
#  <__main__.FuncaoClasse object at 0x100af73d0>
#  >>> FuncaoClasse()()
#  'oi'

# Posso estanciar a FuncaoClasse() para uma outra variável:
#  >>> minha_classe_funcao = FuncaoClasse()
#  >>> minha_classe_funcao()
#  'Oi'

# São funções:
#  >>> type(anonima)
#  <class 'function'>

#  >>> type(funcao_nomeada)
#  <class 'function'>

# Se comporta como uma função mais não é uma função de fato
#  >>> type(FuncaoClasse)
#  <class 'type'>
#  >>> type(FuncaoClasse())
#  <class '__main__.FuncaoClasse'>
#  >>> type(FuncaoClasse().__call__)
#  <class 'method'>
