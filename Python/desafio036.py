# Escreva um programa para aprovar o emrpestimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então ao empréstimo será negado

valorCasa = float(input('Informe o valor da casa R$: '))
valorSalario = float(input('Informe seu salário R$: '))
parcelaAno = int(input('Informe em quantos anos deseja pagar: '))

meses = parcelaAno * 12

mensalidade = valorCasa / meses

parcela_maxima_cliente = valorSalario / 3

if parcela_maxima_cliente > mensalidade:
    print('Empréstimo Aprovado !')
    print('Valor da Casa {:.2f} parcelado em {} mensalidades de R$ {:.2f}'.format(valorCasa, meses, parcela_maxima_cliente))
else:
    print('Empréstimo Negado !')
    print('O valor da mensalidade ultrapassa a PMC(Parcela Máxima Cliente) do cliente de R$ {:.2f}'.format(parcela_maxima_cliente))
