# http://razonartificial.com/2010/02/pygame-2-creando-una-ventana/
# Módulos
import pygame
from pygame.locals import *

# Constantes
WIDTH = 640
HEIGHT = 480
# Clases


# Funciones

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pruebas Pygame')
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0

if __name__ == '__main__':
    pygame.init()
    main()
