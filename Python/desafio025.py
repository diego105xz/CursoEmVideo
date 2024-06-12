# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Informe seu nome: ')

resultado = 'SILVA' in nome.upper()

if resultado:
    print('Seu nome possui SILVA!')
else:
    print('Seu nome não possui SILVA!')