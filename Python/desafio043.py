# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do peso
# -Entre 18.5 e 25: Peso ideal
# -25 até 30: Sobrepeso
# -30 até 40: Obesidade
# -Acima de 40: Obesidade mórbida

altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc =  peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é {:.2f} Categoria: ABAIXO DO PESO.'.format(imc))
elif imc >=18.5 and imc < 25:
    print('Seu IMC é {:.2f} Categoria: PESO IDEAL.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} Categoria: SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} Categoria: OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.2f} Categoria: OBESIDADE MÓRBIDA.'.format(imc))    