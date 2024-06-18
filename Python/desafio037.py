# Escreva um programa que leia um número inteiro qualquer e peça pera o usuário escolher qual será a base de conversão: 

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção digitada incorreta!')