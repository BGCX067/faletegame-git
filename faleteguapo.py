import pygame
import sys
import time
#Iniciar pygame
pygame.init()

# Configurar la ventana
ancho= 1000
alto= 1000 
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
  # Bucle de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
