# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# -À vista dinheiro/cheque: 10% de desconto
# -À vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

produto = float(input('Informe o valor do Produto R$:'))

print('''
FORMAS DE PAGAMENTO:
[ 1 ] Dinheiro/cheque
[ 2 ] Cartão de Credito
''')

opcao = int(input('Informe a forma de pagamento: '))

if opcao == 1:
    descontoDinheiro = (produto * 10)/100
    print('\nForma de pagamento Dinheiro / Cheque')
    print('Valor do produto R$ {:.2f} com desconto de 10%.\n'.format(produto - descontoDinheiro))
    
elif opcao == 2:
    print('\nForma de pagamento Cartão de crédito\n')
    print('PARCELAMENTO:')
    print('[ 1 ] 1X À vista.')
    print('[ 2 ] 2X Vezes.')
    print('[ 3 ] 3X Vezes.')

    opcao = int(input('\nInforme a quantidade de parcelas: '))

    if opcao == 1:
        desoncontoCartao1x = (produto * 5)/100
        print('\nForma de pagamento Cartão de crédito à vista.')
        print('Valor do produto R$ {:.2f} com desconto de 5%.\n'.format(produto - desoncontoCartao1x))
    elif opcao == 2:
        print('\nForma de pagamento Cartão de crédito em 2 vezes.')
        print('Valor do produto R$ {:.2f} .'.format(produto))
        print('Parcelado em 2x de R$ {:.2f}.\n'.format(produto/2))
    elif opcao == 3:
        jurosCartao3x = (produto * 20)/100
        print('\nForma de pagamento Cartão de crédito à vista.')
        print('Valor do produto R$ {:.2f} com juros de 20%.'.format(produto + jurosCartao3x))
        print('Parcelado em 3x de R$ {:.2f}.\n'.format((produto + jurosCartao3x)/3))
    else:
        print('Valor de parcelas inválido!\n')
else:
    print('Opção inválida')