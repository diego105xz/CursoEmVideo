# Codições Part 1
# Estrutura condicional simples só possui IF, e estutura condicional composta possui IF e ELSE, se o if e else estiver na mesma linha vira condição simplificada

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('A Sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6 else 'Estude MAIS!') # Condição simplificada


