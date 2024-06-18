# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários
import random

acertou = int(0)
chance = 0

while acertou == 0:

    numero = int(input('Tente adivinhar o número que estou espensando de 0 a 5: '))

    numeroSorteado = random.randint(0,5)
    chance += 1 
    if numero == numeroSorteado:
        print('VOCê ACERTOU! PARABENS!!!')
        print('Você precisou de {} chances para acertar.'.format(chance))
        acertou = 1
    else:
        print('O número que eu pensei foi {}! VOCÊ ERROU!'.format(numeroSorteado))