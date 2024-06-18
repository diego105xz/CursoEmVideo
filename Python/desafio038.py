# Escreva um programa que leia dois números inteiro e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor maior
# - O segundo valor maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2 :
    print('O primeiro maior número é {}'.format(n1))
    print('O segundo maior número é {}'.format(n2))
elif n2 > n1:
    print('O primeiro maior número é {}'.format(n2))
    print('O segundo maior número é {}'.format(n1))
else:
    print('Não existe valor maior, os dois são iguais')