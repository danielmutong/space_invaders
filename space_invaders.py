import pygame
import random
import math
from pygame import mixer
 



# initializing pygame
pygame.init()
 
# creating screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,
                                  screen_height))
 
# caption and icon
pygame.display.set_caption("Welcome to Space\
Invaders Game by:- styles")
 
# Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)
 
# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
 

 
# Background Sound
mixer.music.load('data/background.wav')
mixer.music.play(-1)
 
# player
playerImage = pygame.image.load('data/spaceship.png')
player_X = 370
player_Y = 523
player_Xchange = 0
 
# Invader
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

#bullets:
bulletImage = pygame.image.load('data/bullet.png')
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 10
bullet_state = "rest"

running = True

#################functions---------------------------------------------------
##############################################
#show_score
##############################################
def show_score(x, y):
    score = font.render("Points: " + str(score_val),
                        True, (255,255,255))
    screen.blit(score, (x , y ))

##############################################
#game_over
############################################## 
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255,255,255))
    screen.blit(game_over_text, (190, 250))

##############################################
#create_invaders
##############################################
def create_invaders():
    global no_of_invaders
    global invaderImage 
    global invader_X 
    global invader_Y 
    global invader_Xchange 
    global invader_Ychange 

    for num in range(no_of_invaders):
        invaderImage.append(pygame.image.load('data/alien.png'))
        invader_X.append(random.randint(64, 737))
        invader_Y.append(random.randint(30, 180))
        invader_Xchange.append(0.2)
        invader_Ychange.append(50)
 

##############################################
#for copy pasta
##############################################
def set_global_var():

    # player
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state , score_val

##############################################
#check_collision
##############################################
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False

##############################################
#draw player
############################################## 
def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))

##############################################
#draw invader
############################################## 
def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

##############################################
#draw bullet
############################################## 
def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"
 
##############################################
#update screen
############################################## 
def update_screen():
    screen.fill((0, 0, 0))

##############################################
#exit cond
############################################## 
def check_exit(event):
    global running
    if event.type == pygame.QUIT:
        running = False

##############################################
#check left
############################################## 
def check_left_key(event):
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_Xchange = -1.7

##############################################
#check right
############################################## 
def check_right_key(event):
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player_Xchange = 1.7
            
##############################################
#check fire
############################################## 
def check_fire(event):
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
        
        # Fixing the change of direction of bullet
            if bullet_state == "rest":
                bullet_X = player_X
                bullet(bullet_X, bullet_Y)
                bullet_sound = mixer.Sound('data/bullet.wav')
                bullet_sound.play()

##############################################
#check no key
############################################## 
def check_no_key(event):
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 
        
    if event.type == pygame.KEYUP:
        player_Xchange = 0

##############################################
#control player
############################################## 
def control_player():
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        check_left_key(event)
        check_right_key(event)
        check_fire(event)
        check_no_key(event)
        
    move_player()

##############################################
#move player
##############################################              
def move_player():
    global player_X, player_Xchange

    player_X += player_Xchange

##############################################
#move bullet
##############################################  
def move_bullet():
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 

        # bullet movement
    if bullet_Y <= 0:
        bullet_Y = 600
        bullet_state = "rest"
    if bullet_state == "fire":
        bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Ychange

##############################################
#move invader
##############################################    
def move_invader():
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state , score_val

    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]
        
    for i in range(no_of_invaders):
        
        if invader_Y[i] >= 450:
            if abs(player_X-invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                    explosion_sound = mixer.Sound('data/explosion.wav')
                    explosion_sound.play()
                game_over()
                break

        if invader_X[i] >= 735.0 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]
        # Collision
        collision = isCollision(bullet_X, invader_X[i],
                                bullet_Y, invader_Y[i])
        if collision:
            score_val += 1
            bullet_Y = 600
            bullet_state = "rest"
            invader_X[i] = random.randint(64, 736)
            invader_Y[i] = random.randint(30, 200)
            #invader_Xchange[i] *= -1
            #speed up if score exceeds
            if score_val == 5:
                for y in range(no_of_invaders):
                    if invader_Xchange[y] > 0:
                        invader_Xchange[y] += 1
                    else:
                       invader_Xchange[y] -= 1 
            if score_val == 10:
                for y in range(no_of_invaders):
                    if invader_Xchange[y] > 0:
                        invader_Xchange[y] += 1
                    else:
                       invader_Xchange[y] -= 1 
                       
            for num in range(no_of_invaders):
                print(str(round(invader_Xchange[num],2)) + '  ', end = '')   
            print('\n')                             
                
        invader(invader_X[i], invader_Y[i], i)

##############################################
#check bounds
##############################################    
def check_bounds():
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 
 
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750
    player(player_X, player_Y)

##############################################
#main
##############################################    
def main():
    global running, playerImage, player_X, player_Y , player_Xchange , invaderImage , invader_X ,invader_Y,invader_Xchange \
    ,invader_Ychange ,no_of_invaders ,bulletImage ,bullet_X ,bullet_Y ,bullet_Xchange ,bullet_Ychange ,bullet_state 
    
    while running: 
        create_invaders()
        update_screen()
        control_player()
        move_invader()
        move_bullet()
        check_bounds()
        show_score(scoreX, scoreY)
        pygame.display.update()

main()