# Refaça o deafio 009, mostrando a tabuada de um número que o usuário escolher, só que afora utilizando um laço for

num = int(input('Informe o número da tabuada: '))

for c in range(0, 11):
    print('{} X {} = {}'.format(num, c, num * c))
