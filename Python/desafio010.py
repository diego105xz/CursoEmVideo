# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere u$1,00 = R$3,27

real = float(input('Informe seu dinheiro em Real: R$ '))

dollar = real / 3.27

dollar_formatacdo = round(dollar, 2)

print('Você pode comprar ${:.2f} dollares'.format(dollar_formatacdo))