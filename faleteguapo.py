import pygame
import sys
import time
#Iniciar pygame
pygame.init()

# Configurar la ventana
ancho= 745	
alto= 560
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("EL CHICO DE LA NAVAJA ESTA BUENISIMO")

#Cambiar de colores
ROJO = (255 , 0, 0)
NEGRO = (0, 0, 0)
COLORES = (ROJO, NEGRO)

for rojo in COLORES:
	ventana.fill(rojo)
	time.sleep(2) 
	pygame.display.update()
 
imagen = pygame.image.load ("img/pistas.jpg")
imagen = imagen.convert()
x,y = (0,0) 
ventana.blit(imagen, [x,y])
pygame.display.flip()

imagen = pygame.image.load ("img/atleta.jpg") 
imagen = imagen.convert()
x,y = (200,200)
ventana.blit(imagen, [x,y])
pygame.display.flip()
  # Bucle de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x = x - 10
				ventana.blit(imagen, [x,y])
				pygame.display.flip()
        if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				x = x + 10
				ventana.blit(imagen, [x,y])
				pygame.display.flip()
