# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Informe o nome da sua cidade: ')

cidadeArray = cidade.split()

verificaSanto = cidadeArray[0].upper()

if verificaSanto == 'SANTO':
    print('Sua cidade começa com a palavra {}'.format(verificaSanto))