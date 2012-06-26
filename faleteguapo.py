import pygame
import sys

#Iniciar pygame
pygame.init()

# Configurar la ventana
ancho= 1000
alto= 1000
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("EL CHICO DE LA NAVAJA ESTA BUENISIMO")


  # Bucle de eventos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
