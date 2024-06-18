# A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SÊNIOR
# Acima: MASTER
import datetime

anoNascimeneto = int(input('Ano de nascimento: '))

anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimeneto

if idade <= 9:
    print('Atleta categoria MIRIM.')
elif idade <= 14:
    print('Atleta categoria INFANTIL.')
elif idade <= 19:
    print('Atleta categoria JUNIOR.')
elif idade <= 20:
    print('Atleta categoria SÊNIOR.')
else:
    print('Atleta categoria MASTER.')

