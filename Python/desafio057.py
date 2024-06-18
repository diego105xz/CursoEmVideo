# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

valorCorreto = 0

while valorCorreto == 0 :

    print('Qual o sexo ?')
    print('[ M ] - Masculino')
    print('[ F ] - Feminino')

    sexo = str(input('Informe o sexo: '))

    if sexo in 'Mm' or sexo in 'Ff':
        valorCorreto = 1
    
print('você digitou o Sexo correto!')