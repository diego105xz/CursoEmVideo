# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

# importar a biblioteca pygame
from pygame import mixer

# uma forma de implementar o código
mixer.init()

# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
mixer.music.load('desafio021.mp3')
mixer.music.play()
x = input('Digite algo para parar...')
