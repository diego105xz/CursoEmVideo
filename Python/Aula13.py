# Estrutura de repetição for

# Exemplo 1
for c in range(0,6):
    print('oi')
print('fim')

# Exemplo 2
for c in range(0,10,2):
    print(c)
print('fim2')

# Exemplo 3
for c in range(10, 0, -1):
    print(c)
print('fim3')

# Exemplo 4
inicio = int(input('Informe o número inicial: '))
fim = int(input('Informe o númeor final: '))
intervalo = int(input('Informe o interval: '))


for c in range(inicio, fim, intervalo):
    print(c)
print('Fim4')