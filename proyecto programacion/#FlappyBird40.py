#Flappy Bird 4.0
#Proyecto de Programación por Karen Andrea Melendez Redondo, Geronimo Rojas Guevara y Alejandro Borja Abad

#170 de diferencia


import pygame
import random

pygame.init()

#Pantalla
size_x = 640/1.25    #Tamaño de pantalla x
size_y = 960/1.25    #Tamaño de pantalla y
fps = 60             #FPS del juego

screen = pygame.display.set_mode([size_x, size_y])  #Pantalla sobre la que se trabajara
timer = pygame.time.Clock()  #Creacion de timer para diferentes procesos

#Imagenes
fondo = pygame.image.load("fondo.png").convert()
fondo = pygame.transform.scale(fondo,(size_x, size_y))  

fbx = size_x/7 #Tamaño de flappy bird en x
fby = ((fbx)/17)*12

arriba = pygame.image.load("arriba.png").convert_alpha()         
arriba = pygame.transform.scale(arriba,(fbx,fby))                                                       

birdy = arriba  #Flappy Bird

bot = pygame.image.load("bot.png").convert_alpha()      
bot = pygame.transform.scale(bot,(fbx*1.3, size_y))   #Tubo de arriba para abajo

top = pygame.image.load("top.png").convert_alpha()      
top = pygame.transform.scale(top,(fbx*1.3, size_y))  #Tubo de abajo para arriba

#Variables
posicion = size_y/2-fby/2   #Posicion de Flappy Bird para referencia
vel = 0          #Cambio de velocidades que tendra flappy bird en el eje y
saltar = 13     #Cuanto saltara el pajaro por aleteo
gravity = 1   #Cuanto bajara cada segundo flappy bird (gravedad)


class tubes(pygame.sprite.Sprite):
    
    def __init__ (self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x , y

    def update (self):
        self.rect.x -= 3 #se mueve 3 pixeles a la izquierda
        if self.rect.x <= -size_x:
            self.kill()

pipes= pygame.sprite.Group()

class flappy(pygame.sprite.Sprite):
    def __init__ (self, x, y, birdy):
        pygame.sprite.Sprite.__init__(self)
        self.image = birdy
        self.posicion = size_y/2-fby/2
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x, y
        
birds = pygame.sprite.Group()
pipe_timer = 0

#Juego en si

volando = True
bird = flappy(150, 150, birdy)
birds.add(bird)
while volando:

    timer.tick(fps)
    screen.blit(fondo,(0,0))
    birds.draw(screen)
    pipes.draw(screen)
    pipes.update()

    if pipe_timer <= 3:
        x_top,x_bottom = 550,550
        y_bottom = random.randint(-700,-280)
        y_top = y_bottom + 170 + bot.get_height() #170 es distancia entre tubos
        pipes.add(tubes(x_top,y_top,bot))
        pipes.add(tubes(x_bottom,y_bottom,top))
        pipe_timer = 200 #cada vez que el timer se termine se hace de nuevo
    pipe_timer -= 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            volando = False
        if event.type == pygame.KEYDOWN:
            for bird in birds:
                if event.key == pygame.K_SPACE:
                    if bird.rect.y - saltar < 1.75 * fby:
                        pass
                    else:
                        vel = - saltar
    for bird in birds:
        if bird.rect.y + vel < size_y - fby:
            bird.rect.y += vel
            vel += gravity
        else:
            bird.rect.y = (size_y - fby)

    #colision 
    for i in birds:
        if pygame.sprite.spritecollide(i, pipes, False):
            
            volando = False

      
    pygame.display.flip()
pygame.quit()


    
