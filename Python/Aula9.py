# Manipulando texto
frase = "Curso em vídeo Python"

# Fatiamento
print(frase[9]) #pega um caracter
print(frase[9:14]) #pega o caracter no range entre 9:14
print(frase[9:21]) #pega o caracter no range entre 9:21
print(frase[9:21:2]) #pega o caracter no range entre 9:21 pulando de 2 em 2
print(frase[:5]) #pega o caracter do inicio até o 5
print(frase[15:]) #pega do caracter 15 até o final
print(frase[9::3]) # pega o caracter 9 até o final e vai pular de 3 em 3
len(frase) #conta quantos caracters tem
frase.count('o') #conta quantas letras o tem na frase
frase.count('o',0,13) #conta quantas letras o tem na frase no range de fatiamento
frase.find('deo') #informa em qual posição do array encontra a pesquisa, caso nã encontre retorna -1
'Curso' in frase # vai retornar true ou false na pesquisa

# Transformação
frase2 = "Curso em Vídeo Python"
frase2.replace('Python', 'Android') # substituir uma palavra por outra
frase2.upper() # Tudo maiusculo
frase2.lower() # Tudo minusculo
frase2.capitalize() # Só o primeiro caracter vai ficar maiusculo
frase2.title() # só a primeira caracter de cara palavra vai ficar maisculo
frase2.strip() # remove espaços no começo e no final da frase que estão atrapalhando a frase
frase2.rstrip() # remove espaço a direita da frase (no final)
frase2.lstrip() # remove espaço a esquerda da frase (no começo)


# Divisão
frase3 = "Curso em Vídeo Python"
frase33 = frase3.split( ) # Divide a string usando o delimitador espaçpo como divisor
# Junção
frase4 = '-'.join(frase33) # Junta a string e adiciona um delimitador
print(frase4)