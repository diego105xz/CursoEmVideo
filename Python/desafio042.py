# Refaça o Desafio dos triângulos, acrescentando o será formado:
# -Equilátero: todos os lados iguais
# -Isósceles: dois lados iguais
# -Escaleno: todos os lados diferentes

print('informe 3 retas')
a = float(input('Primeira reta: '))
b = float(input('segunda reta: '))
c = float(input('terceira reta: '))

retas = [a,b,c]

retas = sorted(retas)
DoisLados = retas[0] + retas[1]
LadoMaior = retas[2]

if DoisLados > LadoMaior:
    print('Pode formar um trinagulo!')
else:
    print('Não é possivel formar um triagulo!')