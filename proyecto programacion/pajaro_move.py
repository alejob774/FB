import pygame, sys, time, random
from pygame.locals import *
    
size_y = 750
size_x = (size_y*(3.25/5))
superficie=pygame.display.set_mode((size_x,size_y))#pantalla (pixeles)
fondo = pygame.image.load("fondo.png").convert()
fondo=pygame.transform.scale(fondo, (size_x,size_y))

arriba=pygame.image.load("arriba.png").convert_alpha() #optimiza la imagen con los mismos pixeles para que no se trabe
arriba=pygame.transform.scale(arriba,(80,80))

medio=pygame.image.load("medio.png").convert_alpha()
medio=pygame.transform.scale(medio,(80,80))

abajo=pygame.image.load("abajo.png").convert_alpha()
abajo=pygame.transform.scale(abajo,(80,80))

imagenes=[arriba,medio,abajo]

fps = pygame.time.Clock()#medir el tiempo 


def main():
    score = 0
    posicion = [200, 150]
    gravedad = 1.5
    vel = 0
    saltar = -35 #cuanto salta el pajaro
    frame = 0  #se cuenta las frames desde el comienzo
    change_sprite = 0 #para que cada 10 frames cambie la imagen 
    
    run=True
    while run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run=False

            if evento.type==pygame.KEYDOWN:#tipo de evento
                if evento.key==pygame.K_SPACE:#tecla para que funcione
                    vel+=saltar

        
        vel+=gravedad 
        vel *= 0.9 #que tan rapido sube y baja el pajaro(cambia de posicion)
        posicion[1]+=vel
        
        superficie.blit(fondo,(0,0)) #foto de fondo sale en pantalla
        imagen=imagenes[change_sprite % 3]#para que se repita las fotos 0,1,2
        superficie.blit(imagen,(int(posicion[0]),int(posicion[1])))
        
        #bordes
        if posicion[1]>=size_y:
            posicion[1]=size_y
            vel=0
            pygame.QUIT()
        elif posicion [1] <= 0:
            posicion[1] = 50
            vel = 0
        print(posicion)
        
        fps.tick(40)#la velocidad con la que baja (frames per second)
        frame += 1
        if frame % 10 == 0:
            change_sprite += 1
        
        pygame.display.flip()
    pygame.quit()
main()