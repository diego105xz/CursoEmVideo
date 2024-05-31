# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe quantos km foram percorridos: '))
dias = int(input('Quantos dias de aluguel do veiculo: '))

valor_dia = 60
valor_km = 0.15

total = (valor_dia * dias) + (km * valor_km)

print(' O valor de dias alugados é R$ {:.2f}\n o valor de km percorridos é R$ {:.2f}\n o valor total a pagar é R$ {:.2f}'.format((valor_dia * dias), (km * valor_km), total))