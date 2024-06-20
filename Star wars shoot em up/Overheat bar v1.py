import pygame
import time
import threading
global x 
running = True
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,255))
x= -20


def coolDown():
    global x
    for i in range(200):
        if x != -20:
            time.sleep(0.01)
            x -= 2
    return x

while running:
    screen.fill((0,0,255))
    t1 = threading.Thread(target = coolDown)
    from pygame.locals import (
            RLEACCEL,
            K_w,
            K_s,
            K_a,
            K_d,
        )

             

    clock = pygame.time.Clock()
    clock.tick(30)
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == K_w:
                        if x <= 378:
                            x += 20
                    if event.key == K_s:
                            t1.start()

        



        
    pygame.draw.rect(screen, (100,100,100),(775,100,25,384))
    pygame.draw.rect(screen, (150,0,0),(777,102,21,x))
    pygame.draw.rect(screen, (100,100,100),(0,100,25,384))
    pygame.draw.rect(screen, (150,0,0),(1,102,21,x))

    pygame.display.flip()
    t1 = threading.Thread(target = coolDown)




   


