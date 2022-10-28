import pygame, sys, time, random
from pygame.locals import *
    
size_y = 750
size_x = (size_y*(3.25/5))
superficie=pygame.display.set_mode((size_x,size_y))#pantalla (pixeles)
fondo = pygame.image.load("fondo.png")
fondo=pygame.transform.scale(fondo, (size_x,size_y))
pajaro=pygame.image.load("medio.png")#pajaro
pajaro=pygame.transform.scale(pajaro,(80,80))
fps = pygame.time.Clock()#medir el tiempo 



def main():
    score = 0
    posicion = [200, 150]
    gravedad = 1.5
    vel = 0
    saltar = -35 #cuanto salta el pajaro
    
    run=True
    while run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run=False

            if evento.type==pygame.KEYDOWN:#tipo de evento
                if evento.key==pygame.K_SPACE:#tecla para que funcione
                    vel+=saltar #cuando se precione espacio el pajaro salta
        
        vel+=gravedad 
        vel *= 0.9 #que tan rapido sube y baja el pajaro(cambia de posicion)
        posicion[1]+=vel
        
        superficie.blit(fondo,(0,0)) #foto de fondo sale en pantalla
        superficie.blit(pajaro,(int(posicion[0]),int(posicion[1])))

       

        pygame.display.flip()
        fps.tick(40)#la velocidad con la que baja (frames per second)
    pygame.quit()
main()