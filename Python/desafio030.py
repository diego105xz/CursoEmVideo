# Crie um program que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

num = int(input('Informe um número: '))

if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))