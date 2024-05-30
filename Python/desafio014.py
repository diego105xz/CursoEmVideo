# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em Celsius: '))

f = (c * 1.8) + 32

print('A temperatura convertida em Fahrenheit é {:.2f}°F'.format(f))