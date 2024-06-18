# Faça um programa que mostre na tela uma contagem regressiva para o estou de fogos de artifício, indo de 10 até 0, com uma pausa de 1s entre eles
import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('Feliz Ano Novo!!!')