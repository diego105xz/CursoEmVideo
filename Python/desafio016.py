# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc


n = float(input('Informe o número: '))

num = trunc(n)

print('O número {} tem a parte inteira {}'.format(n, num))
