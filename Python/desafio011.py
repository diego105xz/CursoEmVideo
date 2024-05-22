# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintála,
# sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))

area = largura * altura

tinta = area / 2

print('Você precisa de {}L de tinta para a pintura'.format(tinta))