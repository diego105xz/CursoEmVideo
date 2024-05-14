# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Informe um número: '))

antecessor = numero - 1
sucessor = numero + 1

print(' O número informado é {}\n seu número antecessor é {}\n seu número sucessor é {}'.format(numero, antecessor, sucessor))