# Opreadores aritiméticos

# + adição
# - subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão inteira
# % Resto da divisão

# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2
# 5 % 2 == 1

# Ordem de precendência
# 1º ()
# 2º **
# 3º * / // % ordem que eles aparece será a ordem para resolver
# 4º + -

print('A'*3)

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

#------------------------------------------------------

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteiro = n1 // n2
exponenciacao = n1 ** n2

print(' A soma é {}\n A multiplicação é {}\n A divisão é {}\n A divisão inteira é {}\n A exponenciação é {}'.format(soma, multiplicacao, divisao, divisaoInteiro, exponenciacao))