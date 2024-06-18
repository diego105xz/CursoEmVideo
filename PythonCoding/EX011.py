# Estruturas de Controle:
# Escreva um programa que verifique se um número é positivo, negativo ou zero.

num = int(input('Informe um número: '))

if num > 0:
    print('O número {} é positivo!'.format(num))

elif num < 0:
    print('O número {} é negativo!'.format(num))

else:
    print('O número {} é neutro'.format(num))