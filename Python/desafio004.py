#Faça um programa que leiia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

dado = input('Digite algo: ')

print('Esse dado é do tipo {}'.format(type(dado)))
print('Só tem espaço?', dado.isspace())
print('É um número?', dado.isnumeric())
print('É Alfabético?', dado.isalpha())
print('É Alfanumérico?', dado.isalnum())
print('Está em maiúsculas?', dado.isupper())
print('Está em minúsculas?', dado.islower())


