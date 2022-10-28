import pygame

def main():
    pygame.init()
    size_sup = 750
    size_lat = (size_sup*(3.25/5))
    superficie=pygame.display.set_mode((size_lat,size_sup))
    fondo = pygame.image.load("fondo.png")
    
    while True:
        evento=pygame.event.poll()
        if evento.type == pygame.QUIT:
            break
        superficie.blit(fondo,(0,0))

        pygame.display.flip()
    pygame.quit()
    
main()