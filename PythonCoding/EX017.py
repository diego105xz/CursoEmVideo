# Estruturas de Controle:
# Escreva um programa que leia três números e imprima-os em ordem crescente.

caracter = str(input('Informe o caracter: '))

vogais = ['a','e','i','o','u']

if caracter.lower() == vogais[0] or caracter.lower() == vogais[1] or caracter.lower() == vogais[2] or caracter.lower() == vogais[3] or caracter.lower() == vogais[4]:
    print('O caracter é uma vogal')
else:
    print('O caracter é uma consoante')