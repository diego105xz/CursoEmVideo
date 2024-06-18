# Estruturas de Controle:
# Escreva um programa que verifique se um número é divisível por 3 e por 5.

num = int(input('Informe um número: '))

if (num % 3 == 0) and ( num % 5 ==0):
    print('O número {} é divisivel por 3 e 5'.format(num))
    print('{} divido por 3 é {}'.format(num, num / 3))
    print('{} divido por 5 é {}'.format(num, num / 5))
else:
    print('O número {} não é divisivel por 3 e 5'.format(num))