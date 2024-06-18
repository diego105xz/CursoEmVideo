# Crie um program que faça o computador jogar jokenpô com você.
import time
import random

print('''JOKENPO!
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA                   
''')

itens = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input('Escolha sua opção: '))
computador = random.randint(0,2)

print('JO')
time.sleep(0.7)
print('KEN')
time.sleep(0.7)
print('PO!!!')
time.sleep(0.7)


if jogador == 0:
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador Jogou {}!'.format(itens[computador]))
    print('Jogador jogou {}!'.format(itens[jogador]))
    print('=-=-=-=-=-=-=-=-=-=-=-=')

    if computador == 0:
        print('EMPATOU!')
    elif computador == 1:
        print('Computador Venceu!')
    else:
        print('Jogador Venceu!')

elif jogador == 1:
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador Jogou {}!'.format(itens[computador]))
    print('Jogador jogou {}!'.format(itens[jogador]))
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    if computador == 0:
        print('Jogador Venceu!')
    elif computador == 1:
        print('EMPATOU!')
    else:
        print('Computador Venceu!')

elif jogador == 2:
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador Jogou {}!'.format(itens[computador]))
    print('Jogador jogou {}!'.format(itens[jogador]))
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    if computador == 0:
        print('Computador Venceu!')
    elif computador == 1:
        print('Jogador Venceu!')
    else:
        print('EMPATOU!')
else:
    print('Jogador escolheu opção inválida')