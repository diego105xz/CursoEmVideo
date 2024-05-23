# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Informe o preço do produto: '))

desconto = (preco_produto * 5 )/100

novo_preco = preco_produto - desconto

print('O Produto com desconto de 5% fica no valor de R$ {:.2f}'.format(novo_preco))