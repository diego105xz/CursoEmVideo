# Estruturas de Controle:
# Escreva um programa que leia dois números e imprima "Aprovado" se a média deles for maior ou igual a 7, caso contrário, imprima "Reprovado".

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2)/2

if media >= 7:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')