# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada l acima do limite.

velocidade = float(input('Informe a velocidade do seu carro: '))

if velocidade > 80:

    kmAcima = velocidade - 80
    multa = kmAcima * 7
    
    print('Você foi Multado!')
    print('Valor da sua multa é R$7,00 por cada km a cima da velocidade maxima')
    print('Valor da Multa R$ {}'.format(multa))
else:
    print('Tenha uma boa viagem!')
