# Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

lista = [n1,n2,n3]

lista = sorted(lista)

print('O Maior número é {}'.format(lista[-1]))
print('O menor número é {}'.format(lista[0]))
    