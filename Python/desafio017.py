# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt

print("Calculadora Hipotenusa.\n")

cateto_oposto = float(input("Informe o cateto oposto: "))
cateto_adjacente = float(input("Informe o cateto adjacente: "))

x = (cateto_oposto ** 2) + (cateto_adjacente ** 2)

hipotenusa = sqrt(x)

print("O valor da hipostenusa {}".format(hipotenusa))