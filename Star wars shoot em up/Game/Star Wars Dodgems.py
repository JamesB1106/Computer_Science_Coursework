# Import the required modules
import pygame
import time
import tkinter as tk
import random
from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_a,
    K_s,
    K_d,
    K_p,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.font.init()
big_font = pygame.font.Font('SWF.ttf', 75)
my_font = pygame.font.Font("SWF.ttf",30)
menu_font = pygame.font.Font('SWF.ttf', 55)
small_menu_font = pygame.font.Font('SWF.ttf', 30)
med_menu_font = pygame.font.Font('SWF.ttf', 50)
base_font = pygame.font.Font('SWF.ttf', 15)
#Variables
menu = True
again = False
scoreboard = False
end = False
loop= True
username = False
running = True
lives = 3
timer = 0
a = 0
points = 0
score = 0
side = 0
float(points)

# Setup for sounds
# pygame.mixer.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
clock.tick(30)

# Define variables for the screen width and height based on resolution
root = tk.Tk()
pygame.display.init()
screenSize = pygame.display.Info()
SCREEN_WIDTH = screenSize.current_w
SCREEN_HEIGHT = screenSize.current_h
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Create a function to draw buttons
def makeButton(oncolour,offcolour,xcoord,ycoord,height,width):
    """oncolour,offcolour,xcoord,ycoord,height,width"""
    #identifies position of mouse
    mouse = pygame.mouse.get_pos()

    #identifies if mouse is clicked
    click = pygame.mouse.get_pressed()    
    #Draws buttons
    if xcoord + width > mouse[0] >xcoord  and ycoord + height > mouse[1] > ycoord:
        pygame.draw.rect(screen, (oncolour),(xcoord,ycoord,width,height))
    else:
        pygame.draw.rect(screen, (offcolour),(xcoord,ycoord,width,height))
    #checks for button press
    if xcoord + width > mouse[0] > xcoord  and ycoord + height > mouse[1] > ycoord:
        if click[0] == 1:
            lives = 3
            menu= False
            startup = False
            running = True
            light = True
            dark = False
            rules = False
    def addText(font,text,text_colour,text_x_coord,text_y_coord):
        #adds text to centre of button
        text_surface = font.render(text, False, text_colour)
        text_rect_center = ((SCREEN_WIDTH/2)-285,SCREEN_HEIGHT/2,)
        screen.blit(text_surface, text_rect_center)
    

# Create custom events for adding a new enemy and cloud
startup = True
while startup:
    while menu:
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop
                if event.key == K_ESCAPE:
                    menu = False
                    startup = False
                    running = False
                    pygame.quit()

            # Did the user click the window close button? If so, stop the loop
            elif event.type == QUIT:
                menu = False
                startup = False
                pygame.quit()
        # pygame.mixer.music.load("SW theme.mp3")
        # pygame.mixer.music.play(loops=-1)
        bgg = pygame.image.load("Menu_screen.png").convert()
        bgg = pygame.transform.scale(bgg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(bgg,(0,0))
        for event in pygame.event.get():
                        # Check for KEYDOWN event
                        if event.type == KEYDOWN:
                            # If the Esc key is pressed, then exit the main loop
                            if event.key == K_ESCAPE:
                                running = False
                        # Check for QUIT event. If QUIT, then set running to false.
                        elif event.type == QUIT:
                            pygame.quit()
        
        #identifies position of mouse
        mouse = pygame.mouse.get_pos()

        #identifies if mouse is clicked
        click = pygame.mouse.get_pressed()    
        #Draws buttons
        if (SCREEN_WIDTH/2)-100 > mouse[0] >(SCREEN_WIDTH/2)-300  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            pygame.draw.rect(screen, (46,103,248),((SCREEN_WIDTH/2)-300,SCREEN_HEIGHT/2-25,200,100))
        else:
            pygame.draw.rect(screen, (15,15,255),((SCREEN_WIDTH/2)-300,SCREEN_HEIGHT/2-25,200,100))
        #checks for button press
        if (SCREEN_WIDTH/2)-100> mouse[0] >(SCREEN_WIDTH/2)-300  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            if click[0] == 1:
                lives = 3
                menu= False
                startup = False
                running = True
                light = True
                dark = False
                rules = False
        #adds text to centre of button
        text_surface = small_menu_font.render('Lightside!', False, (0,0,0))
        text_rect_center = ((SCREEN_WIDTH/2)-285,SCREEN_HEIGHT/2,)
        screen.blit(text_surface, text_rect_center)

        #makes the button "light up" if hovered over by mouse
        if (SCREEN_WIDTH/2)+300 > mouse[0] >(SCREEN_WIDTH/2)+100  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            pygame.draw.rect(screen, (255,51,51),((SCREEN_WIDTH/2)+100,SCREEN_HEIGHT/2-25,200,100))
            #add blueon sfx
        else:
            pygame.draw.rect(screen, (255,0,0),((SCREEN_WIDTH/2)+100,SCREEN_HEIGHT/2-25,200,100))
        #checks for button press
        if (SCREEN_WIDTH/2)+300 > mouse[0] >(SCREEN_WIDTH/2)+100  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            if click[0] == 1:
                lives = 3
                menu= False
                startup = False
                running = True
                light = False
                dark = True
                rules = False
        #adds text to centre of buttons
        text_surface = small_menu_font.render('Darkside!', False, (0,0,0))
        text_rect_center = ((SCREEN_WIDTH/2)+110,SCREEN_HEIGHT/2,)
        screen.blit(text_surface, text_rect_center)
        #Rules button
        if SCREEN_WIDTH -50 > mouse[0] > SCREEN_WIDTH-250  and SCREEN_HEIGHT-50 > mouse[1] > (SCREEN_HEIGHT-150):
            pygame.draw.rect(screen, (148,0,211),(SCREEN_WIDTH-250,SCREEN_HEIGHT-150,200,100))
            #add redon sfx
        else:
            pygame.draw.rect(screen, (128,0,128),((SCREEN_WIDTH-250,SCREEN_HEIGHT-150,200,100)))
        if SCREEN_WIDTH-50 > mouse[0] >SCREEN_WIDTH-250  and (SCREEN_HEIGHT-50) > mouse[1] > (SCREEN_HEIGHT-150):
            if click[0] == 1:
                rules = True
                menu = False
        text_surface = small_menu_font.render('Rules', False, (0,0,0))
        text_rect_center = (SCREEN_WIDTH-200,SCREEN_HEIGHT-125)
        screen.blit(text_surface, text_rect_center)
        pygame.display.flip()
        clock.tick(30)

    #Rules Menu
    while rules == True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    rules = False
                    pygame.quit()
            elif event.type == QUIT:
                rules = False
                pygame.quit()
        img = pygame.image.load("Space.png").convert()
        img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(img, (0,0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 250 > mouse[0] > 50  and SCREEN_HEIGHT-50 > mouse[1] > (SCREEN_HEIGHT-150):
            pygame.draw.rect(screen, (148,0,211),(50,SCREEN_HEIGHT-150,200,100))
        else:
            pygame.draw.rect(screen, (128,0,128),((50,SCREEN_HEIGHT-150,200,100)))
        if 250 > mouse[0] >50  and (SCREEN_HEIGHT-50) > mouse[1] > (SCREEN_HEIGHT-150):
            if click[0] == 1:
                rules = False
                menu = True
        
        text_surface = small_menu_font.render('Return to', False, (0,0,0))
        text_rect_center = (60,SCREEN_HEIGHT-140)
        screen.blit(text_surface, text_rect_center)
        text_surface2 = small_menu_font.render('menu', False, (0,0,0))
        text_rect_center2 = (90,SCREEN_HEIGHT-100)
        screen.blit(text_surface2, text_rect_center2)

        rul = pygame.image.load("Rules.png").convert_alpha()
        screen.blit(rul, (600,150)) 
        pygame.display.flip()

def paused():
    pause = True
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        img = pygame.image.load("Space.png").convert()
        img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(img, (0,0))

        text_surface = big_font.render('Paused', False, (255,255,255))
        text_rect_center = ((SCREEN_WIDTH/2)-150,SCREEN_HEIGHT/4)
        screen.blit(text_surface, text_rect_center)
        #identifies position of mouse
        mouse = pygame.mouse.get_pos()

        #identifies if mouse is clicked
        click = pygame.mouse.get_pressed()    
        #Draws buttons
        if (SCREEN_WIDTH/2)-100 > mouse[0] >(SCREEN_WIDTH/2)-300  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            pygame.draw.rect(screen, (0,255,170),((SCREEN_WIDTH/2)-300,SCREEN_HEIGHT/2-25,200,100))
        else:
            pygame.draw.rect(screen, (0,250,0),((SCREEN_WIDTH/2)-300,SCREEN_HEIGHT/2-25,200,100))
        #checks for button press
        if (SCREEN_WIDTH/2)-100> mouse[0] >(SCREEN_WIDTH/2)-300  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            if click[0] == 1:
                lives = 3
                pause = False
        #adds text to centre of button
        text_surface = small_menu_font.render('Continue', False, (0,0,0))
        text_rect_center = ((SCREEN_WIDTH/2)-285,SCREEN_HEIGHT/2,)
        screen.blit(text_surface, text_rect_center)

        #makes the button "light up" if hovered over by mouse
        if (SCREEN_WIDTH/2)+300 > mouse[0] >(SCREEN_WIDTH/2)+100  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            pygame.draw.rect(screen, (0,255,170),((SCREEN_WIDTH/2)+100,SCREEN_HEIGHT/2-25,200,100))
        else:
            pygame.draw.rect(screen, (0,250,0),((SCREEN_WIDTH/2)+100,SCREEN_HEIGHT/2-25,200,100))
        #checks for button press
        if (SCREEN_WIDTH/2)+300 > mouse[0] >(SCREEN_WIDTH/2)+100  and (SCREEN_HEIGHT/2)+75 > mouse[1] > (SCREEN_HEIGHT/2)-25:
            if click[0] == 1:
                pygame.quit()
                quit()
        #adds text to centre of buttons
        text_surface = small_menu_font.render('quit!', False, (0,0,0))
        text_rect_center = ((SCREEN_WIDTH/2)+110,SCREEN_HEIGHT/2,)
        screen.blit(text_surface, text_rect_center)
        pygame.display.update()
        clock.tick(30)  
if light == True:
    astro = pygame.image.load("astromech.png").convert_alpha()
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load("xwing.png").convert_alpha()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            
        # Move the sprite based on keypresses
        def update(self, pressed_keys):
            if pressed_keys[K_UP] or pressed_keys[K_w] :
                self.rect.move_ip(0, -10)
            if pressed_keys[K_DOWN]or pressed_keys[K_s]:
                self.rect.move_ip(0, 10)
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-10, 0)
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(10, 0)

            # Keep Player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
elif dark == True:
    astro = pygame.image.load("astromech2.png").convert_alpha()
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load("tie.png").convert_alpha()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
            
        # Move the sprite based on keypresses
        def update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 10)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)

            # Keep Player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
    
size = 0
# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite

class  Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        size = random.randint(0,10)
        if size > 8:
            self.surf = pygame.image.load("Asteroid1.png").convert_alpha()
        elif 3 < size <= 8:
            self.surf = pygame.image.load("Asteroid.png").convert_alpha()
        elif size <= 3:
            self.surf = pygame.image.load("Asteroid2.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        if points < 100:
            self.speed = random.randint(5, 15)
        elif 100 <= points < 200:
            self.speed = random.randint(15, 20)
        elif 200 <= points < 300:
            self.speed = random.randint(10, 25)
        elif 300<= points < 400:
            self.speed = random.randint(25, 30)
        elif 400<= points < 500:
            self.speed = random.randint(35,40)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
class Heals(pygame.sprite.Sprite):
    def __init__(self):
        global astro
        super(Heals, self).__init__()
        self.surf = astro
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 150),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        if points < 100:
            self.speed = random.randint(5, 20)
        elif 100 <= points < 250:
            self.speed = random.randint(15, 30)
        elif 250<= points < 500:
            self.speed = random.randint (25, 40)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
clock.tick(30)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create custom events for adding a new enemy and cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDHEALS = pygame.USEREVENT + 2
pygame.time.set_timer(ADDHEALS, random.randint(15000,25000))

# Create our 'Player'
Player = Player()
heals = Heals()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
heals = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(Player)

# Load and play our background music
# pygame.mixer.music.load("SW theme.mp3")
# pygame.mixer.music.play(loops=-1)

menu = True
again = False
scoreboard = False
end = False
loop= True
username = False
lives = 3
timer = 0
a = 0
points = 0
side = 0
float(points)

#Main loop
while running == True:
    #Main game
    # add a  points system
    timer = timer + 1
    if timer % 20 == 0:
        if points < 100:
            points = points + 1
        elif 100 <= points < 200:
            points = points + 1.5
        elif 200 <= points <= 300:
            points = points + 2
        elif 300 <= points <= 400:
            points = points + 2.5
        elif 400 <= points <= 500:
            points = points + 3
        if points >= 500:
            running = False
            #add next level here
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
            elif event.key == K_p:
                paused()

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False
            pygame.quit()


        # Should we add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy, and add it to our sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # Should we add a bonus life?
        elif event.type == ADDHEALS:
                new_heals=Heals()
                heals.add(new_heals)
                all_sprites.add(new_heals)
                print('Healy wealy')

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    Player.update(pressed_keys)

    # Update the position of our enemies and clouds
    enemies.update()
    heals.update()
    
    # Fill the screen with space
    img = pygame.image.load("Space.png").convert()
    img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(img, (0,0))

    #points onscreen
    text_surface = my_font.render('points:'+str(round(points)), False, (255,255,255))   
    if points <10:
        a = 1480
    elif points < 100:
        a = 1460
    elif points < 1000:
        a = 1440
    else:
        a = 1420
    screen.blit(text_surface,(a,0))


    # lives onscreen
    text_surface = my_font.render('lives:'+str(lives), False, (255,255,255))
    screen.blit(text_surface,(SCREEN_WIDTH/2-25,SCREEN_HEIGHT-50))
    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the Player
    if pygame.sprite.spritecollideany(Player, enemies):
        lives -= 1
        Enemy.kill(pygame.sprite.spritecollideany(Player,enemies))
        if lives <=0:
            Player.kill()
            running = False
            pygame.display.flip
    if pygame.sprite.spritecollideany(Player, heals):
        if lives < 3:
            lives += 1
        elif lives ==3:
            points += 25
            score += 100 
        Enemy.kill(pygame.sprite.spritecollideany(Player,heals))
            


    # Flip everything to the display
    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)

# At this point, we're done, so we can stop and quit the mixer
# pygame.mixer.music.stop()
# pygame.mixer.quit()
