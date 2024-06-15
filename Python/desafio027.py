# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = input('Informe seu nome Completo: ')

nome = nome.split()

primeiro = nome[0]
ultimo = nome[-1]

print('Primeiro nome: {}'.format(primeiro))
print('Último nome: {}'.format(ultimo))