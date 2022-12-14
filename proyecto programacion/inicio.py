import pygame, sys, time, random 
from pygame.locals import *
    

size_y = 750
size_x = (size_y*(3.25/5))
superficie=pygame.display.set_mode((size_x,size_y))#pantalla (pixeles)
fondo = pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\fondo.png").convert()
fondo=pygame.transform.scale(fondo, (size_x,size_y))
flappy = pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\flappy.png").convert_alpha()
flappy=pygame.transform.scale(flappy, (450,450))
start = pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\start.png").convert_alpha()
start=pygame.transform.scale(start, (200,200))

arriba=pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\arriba.png").convert_alpha() #optimiza la imagen con los mismos pixeles para que no se trabe
arriba=pygame.transform.scale(arriba,(80,80))

medio=pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\medio.png").convert_alpha()
medio=pygame.transform.scale(medio,(80,80))

abajo=pygame.image.load(r"C:\Users\Jeronimo\OneDrive\Escritorio\PROGRAMACIÓN\abajo.png").convert_alpha()
abajo=pygame.transform.scale(abajo,(80,80))

imagenes=[arriba,medio,abajo,medio]
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
                if 168 <= mouse[0] <= 319 and 540 <= mouse[1] <= 635: #muestra la ubicacion exacta del boton de start
                    pygame.quit()
                
        mouse = pygame.mouse.get_pos() #yuda a tener la ubicacion exacta del mouse

        superficie.blit(fondo,(0,0)) #foto de fondo sale en pantalla
        superficie.blit(flappy,(55,40)) #foto del pajaro
        pajaro=imagenes[change_sprite % 4]#para que se repita las fotos 0,1,2 y 3
        superficie.blit(pajaro,(205,330))
        superficie.blit(start,(142,500))
        



        fps.tick(40)#la velocidad con la que baja (frames per second)
        frame += 1
        if frame % 10 == 0:
            change_sprite += 1
        
        pygame.display.update()
        pygame.font.quit()
        pygame.display.flip()
    pygame.quit()
    
main()