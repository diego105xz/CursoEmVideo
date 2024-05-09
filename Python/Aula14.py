# Estrutura de repetição while

# for c in range(1, 10):
#     print(c)
# print('fim')

# c = 1
# while c < 10:
#     print(c)
#     c += 1 

# print('fim')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')

n = 1
par = 0
impar = 0

while n != 0: #enquanto digitar diferente de '0' continue executando.
    n = int(input('Dígite um número: '))

    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} númeors impares'.format(par, impar))