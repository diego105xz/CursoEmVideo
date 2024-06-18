# Listas e Loops:
# Escreva um programa que encontre o maior elemento de uma lista.

lista = [1,3,5,7,9]

maior_elemento = lista[0]

for elemento in lista:

    if elemento > maior_elemento:
        maior_elemento = elemento

print("O Maior elemento é {}".format(maior_elemento))