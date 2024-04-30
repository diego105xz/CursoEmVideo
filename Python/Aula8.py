# import bebida   Ex: neste caso vai importar todas a bebidas cafe, refri, suco.
# from doce import pudium  Ex: neste caso vai importa da biblioteca doce especificamente pudim.

# biblioteca math "matemática" 
#Funções
# ceil - arrendodamento pra cima
# floor - arrendodamento pra baixo
# trunc - vai eliminar da virgula pra frente
# pow - potencia
# sqrt - raiz quadrada
# factorial - calcular fatorial

# import match -vai importar tudo
# from math import sqrt - vai importa a biblioteca matematica somente a funao necessaria

import math

num = int(input('Digite um núnero: '))

raiz = math.sqrt(num)
# print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))


# a biblioteca radom gera um número aleatório entre 0 e 1
import random 
n = random.random()
print(n)

# gera um número inteiro de 1 a 10
numero = random.randint(1,10)
print(numero)

import emoji

print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))
