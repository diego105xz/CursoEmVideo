# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe seu salário atual: '))

regra_aumento = (salario * 15) / 100

novo_salario = salario + regra_aumento

print('Seu salário teve um aumento de 15% ficando no valor de R$ {:.2f}'.format(novo_salario))