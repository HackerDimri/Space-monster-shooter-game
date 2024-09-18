import pygame
from pygame import mixer
import random
import math
pygame.init()

screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("I dont know")
icon=pygame.image.load("outer-space.png")
pygame.display.set_icon(icon)

background=pygame.image.load("bg.png")

mixer.music.load('moonlight-mastered-4736.mp3')
mixer.music.play(-1)

playerimage=pygame.image.load("pistol.png")
playerx=400
playerxa=0
playery=535

def player(img,x,y):
    screen.blit(img,(x,y))

enemyimage=[]
enemyx=[]
enemyxa=[]
enemyy=[]
noofenemies=6

for i in range (noofenemies):
    enemyimage.append(pygame.image.load("monster.png"))
    enemyx.append(random.randint(0,700))
    enemyxa.append(0.1)
    enemyy.append(random.randint(0,400))

def enemy(img,x,y):
    screen.blit(img,(x,y))

font=pygame.font.Font('freesansbold.ttf', 32)
textx=10
texty=10

def showscore(x,y):
    scoore=font.render("SCORE:"+str(score),True,(255,255,255))
    screen.blit(scoore,(x,y))

font2=pygame.font.Font('freesansbold.ttf', 80)
textx2=200
texty2=300

def got(x,y):
    gameover=font2.render("GAMEOVER",True,(255,255,255))
    screen.blit(gameover,(x,y))

bulletimage=pygame.image.load("bullet.png")
bulletx=playerx+10
bullety=playery
bulletxa=0

def bullet(img,x,y):
    screen.blit(img,(x,y))

fire=0

def collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2))
    if distance<40:
        return True
    else:
        return False

score=0
run=True
a=0

while run:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxa-=0.4
            if event.key==pygame.K_RIGHT:
                playerxa+=0.4
            if event.key==pygame.K_SPACE:
                fire+=1
                bullet(bulletimage,bulletx,bullety)
                bulletxa+=1
                bs=mixer.Sound("SpaceLaserShot PE1095407.mp3")
                bs.play()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                playerxa=0
            if event.key==pygame.K_LEFT:
                playerxa=0                

    playerx=playerx+playerxa
    if playerx <=0:
        playerx=0
    if playerx>=740:
        playerx=740
    for i in range (noofenemies):
        if enemyy[i] >=500:
            for j in range(noofenemies):
                print("work",enemyx,enemyy)
                enemyy[j]=801
                got(textx2,texty2)
            break

        if enemyx[i] >=700:
            enemyxa[i]=-0.1
            enemyy[i]+=10
        if enemyx[i] <=0:
            enemyxa[i]=+0.1
            enemyy[i]+=10
        enemyx[i]+=enemyxa[i]
        colisn=collision(enemyx[i],enemyy[i],bulletx,bullety)
        
        if colisn:
            bullety=playery
            fire=0
            score+=1
            bulletxa=0
            enemyx[i]=random.randint(0,700)
            enemyy[i]=random.randint(0,400)
            enemyx[i]+=enemyxa[i]
            blast=mixer.Sound("GrenadesTntBlast PE1094404.mp3")
            blast.play()
        enemy(enemyimage[i],enemyx[i],enemyy[i])

    if bullety<=0:
        bullety=playery
        fire=0
        bulletxa=0
        
    if fire ==0:
        bulletx=playerx+10
        bullety=playery
    if fire!=0:
        bullety-=bulletxa
        bullet(bulletimage,bulletx,bullety)
    player(playerimage,playerx,playery)
    showscore(textx,texty)
    
    pygame.display.update()
    
