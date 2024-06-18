# Desenvolva um progra que pergunte a distância de uma viagem em km. 
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Informe a distância da viagem em km: '))

if distancia <= 200:
    km = float(0.50)
    preco = distancia * km
    print('O valor da viagem é R$ {}'.format(preco))

else:
    km = float(0.45)
    preco = distancia * km
    print('O valor da viagem é R$ {}'.format(preco))