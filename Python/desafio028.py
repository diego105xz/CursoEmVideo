# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

acertou = int(0)

while acertou == 0:

    numero = int(input('Tente adivinhar o número que estou espensando de 0 a 5: '))

    numeroSorteado = random.randint(0,5)

    if numero == numeroSorteado:
        print('VOCê ACERTOU! PARABENS!!!')
        acertou = 1
    else:
        print('O número que eu pensei foi {}! VOCÊ ERROU!'.format(numeroSorteado))