# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo de que falta ou que passou do prazo.
import datetime

anoNascimento = int(input('Informe seu ano de nascimento: '))

anoAtual = datetime.date.today().year

idade = anoAtual - anoNascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(anoNascimento, idade, anoAtual))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(18 + anoNascimento))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(18 + anoNascimento))