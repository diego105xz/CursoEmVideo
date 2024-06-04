# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.

import random 

print("Gerador de Sorteios")

participante = int(input("Informe a quantidade de participantes: "))

contador = 0
participantes = []

while ( contador < participante):

    participantes.append(input("Informe o nome do participante Nº{} : ".format(contador + 1)))

    contador = contador + 1


numero = len(participantes)

numeroSorteio = random.randint(1, numero)

sorteado = participantes[numeroSorteio - 1]

print("A Pessoa sorteada é {}!".format(sorteado))