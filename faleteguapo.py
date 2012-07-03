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
 
fondo = pygame.image.load ("img/pistas.jpg")
fondo = fondo.convert()
x,y = (0,0) 
ventana.blit(fondo, [x,y])
pygame.display.flip()

personaje = pygame.image.load ("img/atleta.jpg") 
personaje = personaje.convert()
x_personaje,y_personaje = (200,200)
pygame.display.flip()
  # Bucle de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ventana.blit(fondo, [x,y])
                x_personaje = x_personaje -10
                ventana.blit(personaje, [x_personaje,y_personaje])
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                ventana.blit(fondo, [x,y])
                x_personaje = x_personaje + 10
                ventana.blit(personaje, [x_personaje,y_personaje])
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                ventana.blit(fondo, [x,y])
                y_personaje = y_personaje + 10
                ventana.blit(personaje, [x_personaje,y_personaje])
                pygame.display.flip()
            if event.key == pygame.K_UP:
                ventana.blit(fondo, [x,y])
                y_personaje = y_personaje - 10
                ventana.blit(personaje, [x_personaje,y_personaje])
                pygame.display.flip()     
