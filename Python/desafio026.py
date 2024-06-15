# Faça um programa que leia uma frase pelo teclado e mostre:
# 1-Quantas vezes aparece a letra "A"
# 2-Em que posição ela aparece a primeira vez
# 3-Em que posição ela aparece a última vez.

frase = input('Elabore uma frase: ')

frase = frase.lower()
letrasA = frase.count('a')

primeiroA = frase.find('a')
ultimoA = frase.find('a',-1)



print('Temos nessa frase {} letras A'.format(letrasA))
print('A posição da primeira letra A é {}'.format(primeiroA))
print('A ultima posição da letra A é {}'.format(ultimoA))