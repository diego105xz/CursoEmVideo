# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

print("Claculadora de seno, consseno e tangente")

angulo = float(input("Informe o angulo: "))

def calcular_seno(angulo):

    return math.sin(math.radians(angulo))


def calcular_cosseno(angulo):

    return math.cos(math.radians(angulo))


def calcular_tangente(angulo):
    
    return math.tan(math.radians(angulo))



seno = calcular_seno(angulo)
cosseno = calcular_cosseno(angulo)
tangente = calcular_tangente(angulo)

print("O angulo de {}°: ".format(angulo))
print("Seno: {:.2f}°".format(seno))
print("Cosseno: {:.2f}°".format(cosseno))
print("Tangente: {:.2f}°".format(tangente))