# Estruturas de Controle:
# Escreva um programa que compare dois números e imprima o maior deles.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
    print('O número {} é o maior!'.format(n1))
elif n2 > n1:
    print('O número {} é o maior!'.format(n2))
else:
    print('Os números são iguais!')