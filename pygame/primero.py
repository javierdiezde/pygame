# http://razonartificial.com/2010/02/pygame-2-creando-una-ventana/
# Módulos
import pygame, sys
from pygame.locals import *

# Constantes
WIDTH = 640
HEIGHT = 480
# Clases


# Funciones

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pruebas Pygame')

    background_image = load_image('fondoverde.jpg')
    
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
                
        screen.blit(background_image,(0,0))
        pygame.display.flip()
        
    return 0
#-----------------------------------------------------
def load_image(filename, transparent=False):
    # try: image = pygame.image.load(filename)
    # except pygame.error: 
     #    raise SystemExit 
    image=image.convert()
    if transparent:
        color = image.ger_at((0,0))
        image.set_colorkey(color, RLEACCEl)
    return image
#-----------------------------------------------------


if __name__ == '__main__':
    pygame.init()
    main()
