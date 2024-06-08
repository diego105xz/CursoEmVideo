# Crie um programa que leia o nome completo e mostre:
# 1-O nome com todas as letras maiúsculas
# 2-O nome com todas as minúsculas
# 3-Quantas letras ao todo (sem considerar espaços)
# 4-Quantas letras te o primeiro nome

nome = str(input('Informe seu nome completo: '))

nomeMaior = nome.upper()
nomeMenor = nome.lower()

nomeDividido = nome.split()
primeiroNome = nomeDividido[0]
nomeSemEspaco = ''.join(nomeDividido)

print('\nO nome em maiúsculo: {}'.format(nomeMaior))
print('O nome em minúsculo: {}'.format(nomeMenor))
print('Quantas letras ao todo(sem considerar espaços): {}'.format(len(nomeSemEspaco)))
print('Quantas letras tem o primeiro nome {}'.format(len(primeiroNome)))