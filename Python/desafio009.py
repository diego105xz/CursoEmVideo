# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Informe um número: '))

i = 0

while i < 11:
    resultado = n * i

    print('{} x {} = {}'.format(n, i, resultado))
    
    i = i + 1