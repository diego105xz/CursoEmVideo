#Tipos Primitivos

# int 7, -4, 0, 9875
# float 4.5, 0.076, -15.25, 7.0
# bool True, False
# str 'Olá' '7.5'  ''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite ou valor: '))

soma = n1 + n2

#print('A soma entre', n1, 'e', n2, 'vale', soma)
print('A Soma entre {} e {} vale {}'.format(n1, n2, soma))


# verifica o tipo
n = str(input('Digite alguma coisa: '))
print(type(n))