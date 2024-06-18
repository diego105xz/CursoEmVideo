# Crie um programa que leia dois valores e mostre um menu na tela: 
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso

opcao = 0

while opcao != 5:

    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))

    print('Menu')
    print('[1]somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novos números')
    print('[5]sair do programa')

    opcao = int(input('Informe uma das opçõe: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior número.'.format(n1))
        elif n2 > n1:
            print('{} é o maior número.'.format(n2))
        else:
            print('Os números são iguais!')  
    elif opcao == 4:
        print('Insira novos números')
    elif opcao == 5:
        opcao = 5
    else:
        print('Opção incorreta!')


print('Programa finalizado')

