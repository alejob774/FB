import pygame
from pygame.locals import *
import FlappyBirdFinal

height = 960/1.25
width = 640/1.25
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy Bird 4.0")    

fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo,(width, height))                                           
fb = pygame.image.load("FB_WU.png")
fbx = width/7                                                                                  
fby = ((fbx)/17)*12                                                                             
fb = pygame.transform.scale(fb,(fbx,fby))
fbI = pygame.transform.scale(fb,(fbx*2,fby*2))
birdy = fb                                                                                      
tu = pygame.image.load("pipe_top.png")      
tu = pygame.transform.scale(tu,(fbx*1.3, height))                                               
td = pygame.image.load("pipe_bot.png")      
td = pygame.transform.scale(td,(fbx*1.3, height))   

logo = pygame.image.load("Titulo.png")
start = pygame.image.load("Boton-start-flappy.png").convert_alpha()
start = pygame.transform.scale(start, (200,200))

fps = pygame.time.Clock()

def titulo():

    run=True
    while run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run=False
        
            if evento.type==pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos() #yuda a tener la ubicacion exacta del mouse
                if 168 <= mouse[0] <= 319 and 540 <= mouse[1] <= 635: #muestra la ubicacion exacta del boton de start
                    FlappyBirdFinal.juego()

        screen.blit(fondo,(0,0)) #foto de fondo sale en pantalla
        screen.blit(fbI,((width/2)-(fbI.get_width()/2),(height/2)-(fbI.get_height()/2)))
        screen.blit(start,(142,500))
        
        screen.blit(logo, ((width/2)-(logo.get_width()/2), height/ 6))

        fps.tick(60)#la velocidad con la que baja (frames per second)

        pygame.display.update()
        pygame.font.quit()
        pygame.display.flip()
    pygame.QUIT

titulo()
