print ("PRUEBA 1")
a=10
b=0
import pygame
import sys
Reloj= pygame.time.Clock()
from pygame.locals import *
pygame.init()
Ventana = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Moviendo Imágenes")
Imagen = pygame.image.load("ball.gif")
imagen2= pygame.image.load("arco.jpg")

coordX = 300
coordY = 000
Coordenadas = (coordX, coordY)

coord2X=000
coord2Y=000
cordenadas2=(coord2X,coordY)

incrementoX = 0
incrementoY = 0

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Imagen, Coordenadas)
    Ventana.blit(imagen2,cordenadas2)
    pygame.display.flip()

   # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                sys.exit()
            elif evento.key == pygame.K_RIGHT:
                incrementoX = 0.1
                print (incrementoX)
            elif evento.key == pygame.K_LEFT:
                incrementoX = -0.1
                b=b+1
                print (b)
                if(b==13):
                    print("Golll")
                    exit()            
        if evento.type == pygame.KEYUP:
            incrementoX = 0
            incrementoY = 0

    coordX = coordX + incrementoX
    coordY = coordY + incrementoY
    Coordenadas = (coordX, coordY)
