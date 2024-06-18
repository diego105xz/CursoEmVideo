# Estruturas de Controle:
# Escreva um programa que leia três números e imprima-os em ordem crescente.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro númeor: '))

lista = [n1,n2,n3]

print('Ordem original {}'.format(lista))
print('Ordem ordenada {}'.format(sorted(lista)))