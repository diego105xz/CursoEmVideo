# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c 
print('Valor final da soma é {}'.format(soma))