# Estruturas de Controle:
# Escreva um programa que calcule o preço final de um produto com base no preço original e na porcentagem de desconto fornecida pelo usuário.

produto = float(input('Informe o preço do produto: R$ '))
desconto = float(input('Informe o desconto em porcentagem(%): '))

ValorDesconto = (produto * desconto)/100
produtoDesconto = produto - ValorDesconto


print('Valor do produto R$ {:.2f}'.format(produto))
print('Desconto aplicado {}%'.format(desconto))
print('Desconto R$ {:.2f}'.format(ValorDesconto))
print('Novo preço R$ {:.2f}'.format(produtoDesconto))
