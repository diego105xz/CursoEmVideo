# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

anoAtual = datetime.date.today().year

maiorIdade = 0
menorIdade = 0

for c in range(1, 8):
    anoNascimento = int(input('Informe a data de nascimento da {}º criança: '.format(c)))

    idade = anoAtual - anoNascimento

    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print('Das 7 criaças {} delas são de maior de  idade, e {} delas são menor de idade.'.format(maiorIdade, menorIdade))


