# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Informe quantos metros: '))

centimetros = metros * 100

milimetros = metros * 1000

print(' A quantidade de {}m metros convertido para centmetros é {}cm e convertido em milimetros {}mm'.format(metros, centimetros, milimetros))