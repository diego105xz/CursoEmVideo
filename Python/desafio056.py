# Desenvolva um progra que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: 
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaIdade = 0
menorDevinte = 0

for c in range(1, 5):
    
    nome = str(input('\nNome da {}º Pessoa: '.format(c)))
    idade = int(input('Idade da {}º Pessoa: '.format(c)))
    print('Qual sexo ?')
    print('[ M ] - Masculino')
    print('[ F ] - Feminino')
    sexo = str(input('Digite o número correspondente: '))

    somaIdade += idade

    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomevelho = nome

    if idade < 20 and sexo in 'Ff':
        menorDevinte += 1





mediaIdade = somaIdade / 4
print('\nA Média idade do grupo é {:.0f} anos.'.format(mediaIdade))
print('O nome do homem mais velho é {}.'.format(nomevelho))
print('Tem {} mulheres com menos de 20 anos.'.format(menorDevinte))


