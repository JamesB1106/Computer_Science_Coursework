# Import the required modules
import pygame
import tkinter as tk
import random
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_a,
    K_s,
    K_d,
    K_p,
    K_r,
    K_x,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)
#initialise font
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
reload = True
cooldown = False
counter = 0
enemyShoot = 0
lives = 3
timer = 0
a = 0
points = 0
score = 0
side = 0
float(points)

# Setup for sounds
pygame.mixer.init()

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
# runs startup screen
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
        #load and play music
        pygame.mixer.music.load("SW theme.mp3")
        pygame.mixer.music.play(loops=-1)
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
        #load background
        img = pygame.image.load("Space.png").convert()
        img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(img, (0,0))
        #get mouse stuff
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
#create a pause screen
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
        text_rect_center = ((SCREEN_WIDTH/2)+140,SCREEN_HEIGHT/2,)
        screen.blit(text_surface, text_rect_center)
        pygame.display.update()
        clock.tick(30)
#Allows user to switch between light and dark side        
if light == True:
    astromech = "astromech.png"
    usersprite = "xwing.png"
    bullet = "Redlaser.png"
    enemyPic = "tie2.png"
elif dark == True:
    astromech = "astromech.png"
    usersprite = "tie.png"
    bullet = "Greenlaser.png"
    enemyPic = "xwing2.png"

astro = pygame.image.load(astromech).convert_alpha()
#build player class
class Player(pygame.sprite.Sprite):
    #initialise player
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(usersprite).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=((SCREEN_WIDTH/2),SCREEN_HEIGHT-1))
    #functions that allow player to shoot
    def shoot1(self):
        if reload:
            bullet = Bullet((self.rect.centerx+30), self.rect.top)
            bullets.add(bullet)
            all_sprites.add(bullet)
    def shoot2(self):
        if reload:
            bullet = Bullet((self.rect.centerx-30), self.rect.top)
            bullets.add(bullet)
            all_sprites.add(bullet)
    #Move the sprite based on keypresses
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

size = 0
#create the bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load(bullet).convert_alpha()
       #The starting position is set to the 2 guns on the ship
        self.rect = self.surf.get_rect(center = (x,y))
        self.speed = -35

    # Move the bullet based on speed
    # Remove it when it reaches edge of screen
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom < 0:
            self.kill()

        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.speed = 10
        self.surf = pygame.image.load(enemyPic).convert_alpha()
        self.rect = self.surf.get_rect(center=(20,20))

    # Move the enemy based on speed
    # Remove it when it gets shot
    def update(self):
        self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
            self.rect.bottom += 50
            self.speed = 10
            
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.rect.bottom += 50
            self.speed = -10
    def spawnRate(self):
        if points < 100:
            return 1500
        elif 100<= points < 200:
            return 1400
        elif 200<= points < 300:
            return 1300
        elif 300<= points < 400:
            return 1200
        elif 400<= points < 500:
            return 1100
        elif points >= 500:
            return 1000
    def fire1(self):
        bullet = Bullet((self.rect.centerx+30), self.rect.top)
        bullets.add(bullet)
        all_sprites.add(bullet)
    def fire2(self):
        bullet = Bullet((self.rect.centerx-30), self.rect.top)
        bullets.add(bullet)
        all_sprites.add(bullet)
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
pygame.time.set_timer(ADDENEMY, Enemy.spawnRate(Enemy))
ADDHEALS = pygame.USEREVENT + 2
pygame.time.set_timer(ADDHEALS, random.randint(15000,25000))

# Create our 'Player'
Player = Player()
heals = Heals()
bullets = Bullet(0,0)
# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
heals = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(Player)

# Load and play our background music
pygame.mixer.music.load("SW theme.mp3")
pygame.mixer.music.play(loops=-1)

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
gamecounter = 0

#Main loop
while running == True:
    #Main game
    if points >= 500:
        running = False
        #add next level here
    gamecounter += 1    
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
            elif event.key == K_x or event.key == K_SPACE:
                Player.shoot1()
                Player.shoot2()
                counter += 1
                if ammo == 0:
                    reload = False
                else:
                    reload = True
            elif event.key == K_r:
                counter = 0              
                reload = True
        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False
            pygame.quit()

        enemyShoot +=1
        rNg = random.randint(10,30)
        if enemyShoot % rNg == 0:
            enemies.sprites
            enemies.sprites
        
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


    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    Player.update(pressed_keys)

    # Update the position of all non-player sprites
    enemies.update()
    heals.update()
    bullets.update()
    # Fill the screen with the bg
    img = pygame.image.load("Space.png").convert()
    img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(img, (0,0))

    #points onscreen
    text_surface = my_font.render('points:'+str(round(points)), False, (255,255,255))   
    a = SCREEN_WIDTH - (SCREEN_WIDTH/7)
    screen.blit(text_surface,(a,0))


    # lives onscreen
    text_surface = my_font.render('lives:'+str(lives), False, (255,255,255))
    screen.blit(text_surface,(SCREEN_WIDTH/2-25,SCREEN_HEIGHT-50))


    #Bullets on screen
    if counter <= 20:
        ammo = 40 - (counter * 2)
    else:
        ammo = 0
        counter = 20
    if ammo == 0:
        cooldown = True
    if cooldown and ammo <= 30:        
        if gamecounter % 40 == 0:
            counter -= 5
            reload = False
    if ammo == 40:
        reload = True
    text_surface = small_menu_font.render(("Bullets remaining: " + str(ammo)), False, (255,255,255))
    screen.blit(text_surface, (SCREEN_WIDTH-(SCREEN_WIDTH / 4),SCREEN_HEIGHT - (SCREEN_HEIGHT/10)))
    

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
    if pygame.sprite.groupcollide(bullets, enemies,True,True):
        points += 1
    if pygame.sprite.groupcollide(bullets, heals,True,True):
        if lives < 3:
            lives += 1
        elif lives ==3:
            points += 25
            score += 100
            
    # Flip everything to the display
    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)

#At this point, we're done, so we can stop and quit the mixer
pygame.mixer.music.stop()
pygame.mixer.quit()
