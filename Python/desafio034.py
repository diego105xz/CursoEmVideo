# Escreva um programa que pergunte o salário de um funcionário e a calcule o valor do seu aumento.
# Para salários superiores a R$ 1250, calcule um aumento de 10%
# Para os inferiores ou iguais , o aumento é de 15%

salario = float(input('Informe seu salário R$: '))

if salario > 1250:
    aumento = (salario * 10)/100
    novoSalario = salario + aumento
    print('Seu aumento foi de 10% no valor de R$ {}'.format(aumento))
    print('Seu novo salário é R$ {}'.format(novoSalario))
else:
    aumento = (salario * 15)/100
    novoSalario = salario + aumento
    print('Seu aumento foi de 15% no valor de R$ {}'.format(aumento))
    print('Seu novo salário é R$ {}'.format(novoSalario))