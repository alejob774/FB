import pygame, sys, time, random 
from pygame.locals import *
    

size_y = 750
size_x = (size_y*(3.25/5))
superficie=pygame.display.set_mode((size_x,size_y))#pantalla (pixeles)
fondo = pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\fondo.png").convert()
fondo=pygame.transform.scale(fondo, (size_x,size_y))
final_screen = pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\game_over.png").convert_alpha()
final_screen=pygame.transform.scale(final_screen, (450,300))
medio=pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\medio.png").convert_alpha()
medio=pygame.transform.scale(medio,(80,80))


fps = pygame.time.Clock()#medir el tiempo 



def main():
    frame = 0  #se cuenta las frames desde el comienzo
    change_sprite = 0 #para que cada 10 frames cambie la imagen 
    

    run=True
    while run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run=False
        
            if evento.type==pygame.MOUSEBUTTONDOWN:
                if 289 <= mouse[0] <= 402 and 340 <= mouse[1] <= 430: #muestra la ubicacion exacta del boton de start
                    pygame.quit()
                
        mouse = pygame.mouse.get_pos() #yuda a tener la ubicacion exacta del mouse
        
        superficie.blit(fondo,(0,0)) #foto de fondo sale en pantalla
        superficie.blit(final_screen,(18,175))
        superficie.blit(medio,(210,685))

        



        
        
        pygame.display.update()
        pygame.font.quit()
        pygame.display.flip()
    pygame.quit()
    
main()