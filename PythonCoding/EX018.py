# Estruturas de Controle:
# Escreva um programa que leia o ano de nascimento de uma pessoa e imprima se ela é maior de idade ou não.
from datetime import date


anoNascimento = int(input('Informe o seu ano de nascimento: '))

anoAtual = date.today().year

idade = anoAtual - anoNascimento

if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')