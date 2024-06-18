# Estruturas de Controle:
# Escreva um programa que verifique se um número é par ou ímpar.

num = int(input('Informe um número: '))

if num % 2 == 0:
    print('O número {} é Par'.format(num))
else:
    print('O número {} é Ímpar'.format(num))