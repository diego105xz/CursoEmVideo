# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quarto alunos e mostre a ordem sorteada.
from random import shuffle

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4]

shuffle(lista)
print('A origem de apresentação será ')
print(lista)