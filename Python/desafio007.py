# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Informe a primeria nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

print('Sua média é {:.1f}'.format(media))