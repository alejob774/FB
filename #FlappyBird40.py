#Flappy Bird 4.0
#Proyecto de Programación por Karen Andrea Melendez Redondo, Geronimo Rojas Guevara y Alejandro Borja Abad

#170 de diferencia


import pygame
import random

pygame.init()

#Pantalla
width = 640/1.25                                                                                #Tamaño de pantalla x
height = 960/1.25                                                                               #Tamaño de pantalla y
fps = 60                                                                                        #FPS del juego

pygame.display.set_caption("Flappy Bird 4.0")                                                   #Para que la pestaña tenga el nombre de flappy bird
screen = pygame.display.set_mode([width, height])                                               #Pantalla sobre la que se trabajara
timer = pygame.time.Clock()                                                                     #Creacion de timer para diferentes procesos

#Imagenes
fondo = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/fondo.png")
fondo = pygame.transform.scale(fondo,(width, height))                                           #Fondo
fb = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/FB_WU.png")         
fbx = width/7                                                                                   #Tamaño de flappy bird en x
fby = ((fbx)/17)*12                                                                             #Tamaño de flappy bird en y
fb = pygame.transform.scale(fb,(fbx,fby))                                                       
birdy = fb                                                                                      #Flappy Bird
tu = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/pipe_top.png")      
tu = pygame.transform.scale(tu,(fbx*1.3, height))                                               #Tubo de arriba para abajo
td = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/pipe_bot.png")      
td = pygame.transform.scale(td,(fbx*1.3, height))                                               #Tubo de abajo para arriba

#Variables
pos_y = height/2-fby/2                                                                          #Posicion de Flappy Bird para referencia
s_y = 0                                                                                         #Cambio de velocidades que tendra flappy bird en el eje y
wing = 13                                                                                       #Cuanto saltara el pajaro por aleteo
gravity = 0.8                                                                                   #Cuanto bajara cada segundo flappy bird (gravedad)


class tubes(pygame.sprite.Sprite):
    
    def __init__ (self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x , y

    def update (self):
        self.rect.x -= 3
        if self.rect.x <= -width:
            self.kill()

pipe_timer =0
pipes= pygame.sprite.Group()

#Juego en si

volando = True
while volando:

    timer.tick(fps)
    screen.blit(fondo,(0,0))

    screen.blit(birdy,((width/5.5),(pos_y)))

    pipes.draw(screen)
    pipes.update()

    if pipe_timer <= 3:
        x_top,x_bottom = 550,550
        y_bottom = random.randint(-700,-280)
        y_top = y_bottom + 170 + td.get_height()
        pipes.add(tubes(x_top,y_top,td))
        pipes.add(tubes(x_bottom,y_bottom,tu))
        pipe_timer = 200
    pipe_timer -= 2



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            volando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pos_y - wing < 1.75 * fby:
                    pass
                else:
                    s_y = - wing
    
    if pos_y + s_y < height - fby:
        pos_y += s_y
        s_y += gravity
    else:
        pos_y = (height - fby)

    




    pygame.display.flip()
pygame.quit()

    