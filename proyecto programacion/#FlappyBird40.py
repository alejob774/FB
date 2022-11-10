#Flappy Bird 4.0
#Proyecto de Programación por Karen Andrea Melendez Redondo, Geronimo Rojas Guevara y Alejandro Borja Abad

#170 de diferencia


import pygame
import random

pygame.init()

#Pantalla
width = 640/1.25
height = 960/1.25
fps = 60

pygame.display.set_caption("Flappy Bird 4.0")
screen = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()

#Imagenes
fondo = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/fondo.png")
fondo = pygame.transform.scale(fondo,(width, height))
fb = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/FB_WU.png")
fbx = width/7
fby = ((fbx)/17)*12
fb = pygame.transform.scale(fb,(fbx,fby))
birdy = fb
tu = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/pipe_top.png")
tu = pygame.transform.scale(tu,(fbx*1.3, height))
td = pygame.image.load("/Users/alejandroborja/Documents/U/I/Programacion/FB/pipe_bot.png")
td = pygame.transform.scale(td,(fbx*1.3, height))

#Variables
pos_y = height/2-fby/2
s_y = 0
wing = 13
gravity = 0.9


class tubes:
    def __init__ (self):
        h = random.randint(220, 648)
        self.x = width + fbx*1.3
        self.yd = height + h
        self.yu = -height -170 +h
        self.pictd = td
        self.pictu = tu

    def update (self, pos):
        self.x -= 400
        if self.x <= (-width/7*1.3*2):
            self.kill()

    def gameover (self, birdy):
        gameover = False
        


#Juego en si
volando = True
while volando:

    timer.tick(fps)
    screen.blit(fondo,(0,0))

    screen.blit(birdy,((width/5.5),(pos_y)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            volando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pos_y - wing < 1.75*fby:
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

    