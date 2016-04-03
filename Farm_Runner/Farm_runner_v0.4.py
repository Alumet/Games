# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:47:31 2015

@author: Alumet
New Runner project using pygame
Final goal is to test pygame android implementation capabilities
"""

import pygame,random,pickle,os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

(width, height) = (1024,576)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('FARM RUNNER v0.4')
icon = pygame.image.load("./graphics/icon.png").convert_alpha()
pygame.display.set_icon(icon)

pygame.init()
clock = pygame.time.Clock()



#graphics load
pygame.mixer.music.load("./graphics/music.mp3")

landscape = pygame.image.load("./graphics/landscape.png").convert_alpha()
sky = pygame.image.load("./graphics/sky.png").convert_alpha()

cloud_1 = pygame.image.load("./graphics/cloud_1.png").convert_alpha()
cloud_2 = pygame.image.load("./graphics/cloud_2.png").convert_alpha()
cloud_3 = pygame.image.load("./graphics/cloud_3.png").convert_alpha()
cloud_4 = pygame.image.load("./graphics/cloud_4.png").convert_alpha()
clouds=[cloud_1,cloud_2,cloud_3,cloud_4]

ground = pygame.image.load("./graphics/ground.png").convert_alpha()
grass = pygame.image.load("./graphics/grass.png").convert_alpha()

tree_1 = pygame.image.load("./graphics/tree_1.png").convert_alpha()
tree_2 = pygame.image.load("./graphics/tree_2.png").convert_alpha()
tree_3 = pygame.image.load("./graphics/tree_3.png").convert_alpha()
trees=[tree_1,tree_2,tree_3]

cow = pygame.image.load("./graphics/cow.png").convert_alpha()
fence = pygame.image.load("./graphics/fence.png").convert_alpha()
botte = pygame.image.load("./graphics/botte.png").convert_alpha()
sheep = pygame.image.load("./graphics/sheep.png").convert_alpha()
badies=[cow,fence,botte,sheep]

player_1=pygame.image.load("./graphics/player_1.png").convert_alpha()
player_2=pygame.image.load("./graphics/player_2.png").convert_alpha()
player_3=pygame.image.load("./graphics/player_3.png").convert_alpha()
player_4=pygame.image.load("./graphics/player_4.png").convert_alpha()
player_5=pygame.image.load("./graphics/player_5.png").convert_alpha()
player_6=pygame.image.load("./graphics/player_6.png").convert_alpha()
player_7=pygame.image.load("./graphics/player_7.png").convert_alpha()
player_8=pygame.image.load("./graphics/player_8.png").convert_alpha()
player_9=pygame.image.load("./graphics/player_9.png").convert_alpha()
player_10=pygame.image.load("./graphics/player_10.png").convert_alpha()
player_11=pygame.image.load("./graphics/player_11.png").convert_alpha()
player_12=pygame.image.load("./graphics/player_12.png").convert_alpha()
player_13=pygame.image.load("./graphics/player_13.png").convert_alpha()
player_images=[player_1,player_2,player_3,player_4,player_5,player_6,player_7,player_8,player_9,player_10,player_11,player_12,player_13]

number_0=pygame.image.load("./graphics/0.png").convert_alpha()
number_1=pygame.image.load("./graphics/1.png").convert_alpha()
number_2=pygame.image.load("./graphics/2.png").convert_alpha()
number_3=pygame.image.load("./graphics/3.png").convert_alpha()
number_4=pygame.image.load("./graphics/4.png").convert_alpha()
number_5=pygame.image.load("./graphics/5.png").convert_alpha()
number_6=pygame.image.load("./graphics/6.png").convert_alpha()
number_7=pygame.image.load("./graphics/7.png").convert_alpha()
number_8=pygame.image.load("./graphics/8.png").convert_alpha()
number_9=pygame.image.load("./graphics/9.png").convert_alpha()
numbers=[number_0,number_1,number_2,number_3,number_4,number_5,number_6,number_7,number_8,number_9]

life=pygame.image.load("./graphics/life.png").convert_alpha()

menu_font=pygame.image.load("./graphics/menu_font.png").convert_alpha()
title=pygame.image.load("./graphics/title.png").convert_alpha()
play=pygame.image.load("./graphics/play.png").convert_alpha()
foot_note=pygame.image.load("./graphics/foot.png").convert_alpha()
music_signe=pygame.image.load("./graphics/music_signe.png").convert_alpha()
no_music=pygame.image.load("./graphics/no_music.png").convert_alpha()
tuto_image=pygame.image.load("./graphics/tuto.png").convert_alpha()


scrolling_speeds=[1,3,6]

horizon_1=[]#clouds
horizon_2=[]#landscape
horizon_3=[]#grass
horizon_4=[]#trees
horizon_5=[]#badies
horizon_6=[]#ground
horizon_7=[]#player


pygame.mixer.music.play(1000,0.5)


def save():
    global best_scores
    with open('saves','wb') as fichier:
        mon_pickler=pickle.Pickler(fichier)
        mon_pickler.dump(best_scores)
        
def load():
    global best_scores
    with open('saves','rb') as fichier:
        mon_depickler=pickle.Unpickler(fichier)
        best_scores=mon_depickler.load()

try:
    load()
except:
    best_scores=[1000000000,1000000000,1000000000,1000000000]
    save() 
load()

class obj_game():
    
    def __init__(self,obj_type,X=1124):
        
        global scrolling_speeds
        
        self.pose_x=X
        self.type=obj_type
        
        if self.type=="tree":
            global trees
            self.image=random.choice(trees)
            self.pose_y=235
            self.scrolling_speed=scrolling_speeds[2]
            
        if self.type=="cloud":
            global clouds
            self.image=random.choice(clouds)
            self.pose_y=random.randint(0,200)
            self.scrolling_speed=scrolling_speeds[0]
            
        if self.type=="ground":
            global ground
            self.image=ground
            self.pose_y=526
            self.scrolling_speed=scrolling_speeds[2]
            self.pose_x=0
            
        if self.type=="grass":
            global grass
            self.image=grass
            self.scrolling_speed=scrolling_speeds[2]
            self.pose_y=506
            self.pose_x=0
            
        if self.type=="badies":
            global badies
            self.image=random.choice(badies)
            self.scrolling_speed=scrolling_speeds[2]
            self.pose_y=446
        
        if self.type=="landscape":
            global landscape
            self.image=landscape
            self.scrolling_speed=scrolling_speeds[1]
            self.pose_y=230
            self.pose_x=-10
    
    def pose_update(self):
        self.pose_x-=self.scrolling_speed/3
    
    def recycle(self):
        if self.type=="tree" and self.pose_x<-350:
            global trees            
            self.pose_x=1124
            self.image=random.choice(trees)
            
        if self.type=="cloud" and self.pose_x<-350:
            global clouds
            self.pose_x=1124
            self.pose_y=random.randint(0,150)
            self.image=random.choice(clouds)
            
        if self.type=="badies" and self.pose_x<-350:
            global badies
            self.pose_x=random.randint(1124,1324)
            self.image=random.choice(badies)
            
        if self.type=="grass" and self.pose_x<-1258:
            self.pose_x=0
        
        if self.type=="ground" and self.pose_x<-1739:
            self.pose_x=0
         
        if self.type=="landscape" and self.pose_x<-3216:
            self.pose_x=-10

def colision():
    global horizon_7
    global horizon_5
    
    for obj in horizon_5:
        if obj.pose_x in range(250,370) and horizon_7[0].pose_y in range(466,666):
            return True
    return False
    
class player():
    def __init__(self):
        global player_images
        self.pose_x=350
        self.pose_y=466
        self.image=player_images[0]
        self.jump=False
        self.jump_double=False
        self.speed_y=0
        self.animation_state=0
        self.image_state=0
        
    def jump_start(self):
        
        if self.jump==False:
            self.jump=True
            self.speed_y=4.5
        elif self.jump==True and self.jump_double==False:
            self.speed_y=4.5
            self.jump_double=True
        
    def pose_update(self):
        self.speed_y-=0.075
        if self.jump==True:
            self.pose_y-=self.speed_y
        if self.pose_y>466:
            self.pose_y=466
            self.jump=False
            self.jump_double=False
            
        global player
        animation_speed=5
        self.animation_state+=1

        if self.animation_state>animation_speed:
            self.animation_state=0
            if self.image_state==12:
                self.image_state=0
            else:
                self.image_state+=1
        self.image=player_images[self.image_state]
        

for i in range (0,5):
    horizon_1.append(obj_game("cloud",i*300))
    
for i in range (0,3):
    horizon_4.append(obj_game("tree",i*400))

horizon_2.append(obj_game("landscape"))

horizon_3.append(obj_game("grass"))

horizon_6.append(obj_game("ground"))
    
life_nb=3
    
playing=False
menu=True
music=True
tuto=False

while menu:
    pygame.mouse.set_visible(True)
    screen.fill((255,255,255))   
    screen.blit(sky,(0,0))
        
    for obj in horizon_1:
        obj.recycle()
        obj.pose_update()
        screen.blit(obj.image,(obj.pose_x,obj.pose_y))
    
    for obj in horizon_2:
        obj.recycle()
        obj.pose_update()
        screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
    for obj in horizon_3:
        obj.recycle()
        obj.pose_update()
        screen.blit(obj.image,(obj.pose_x,obj.pose_y))
    
    for obj in horizon_4:
        obj.recycle()
        obj.pose_update()
        screen.blit(obj.image,(obj.pose_x,obj.pose_y))
    
    for obj in horizon_6:
        obj.recycle()
        obj.pose_update()
        screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
    screen.blit(menu_font,(0,0))
    
    score_pose=-1
    for score in best_scores:
        score_pose+=1
        score_string=str(score)
        nb_position=-1
        for n in score_string[1:len(score_string)-2]:
            nb_position+=1
            nb=int(n)
            screen.blit(numbers[nb],(nb_position*40+375,320+60*score_pose))

       
    
    screen.blit(play,(375,170))
    screen.blit(title,(10,5))
    screen.blit(foot_note,(5,550))
    screen.blit(music_signe,(940,490))
    
    if music==False:
        screen.blit(no_music,(920,473))

    
    for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                playing= menu=False
            
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                menu=False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                (click_x,click_y) = pygame.mouse.get_pos()
                
                if click_x in range (390,630) and click_y in range(180,250):
                    playing=True
                    horizon_5=[]
                    
                    for i in range (0,4):
                        horizon_5.append(obj_game("badies",i*400+1000))
                        
                    horizon_7=[]
                    horizon_7.append(player())
                    
                    life_nb=3
                    score=1000000000
                    cool_down=201
                    tuto=True
                    pygame.mouse.set_visible(False)
                    
                if click_x in range (940,1024) and click_y in range(490,576):
                    if music==True:
                        pygame.mixer.music.pause()
                        music=False
                    else:
                        pygame.mixer.music.unpause()
                        music=True
    
    while tuto:

        screen.fill((255,255,255))   
        screen.blit(sky,(0,0))
            
        for obj in horizon_1:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        for obj in horizon_2:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
            
        for obj in horizon_3:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        for obj in horizon_4:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        for obj in horizon_6:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
            
        screen.blit(menu_font,(0,0))
        screen.blit(tuto_image,(120,15))
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                playing=True
                tuto=False
    
            if event.type == pygame.QUIT:
                menu=False
                tuto=False
                playing=False
            
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                tuto=False
                playing=False
   
        pygame.display.flip()
        clock.tick_busy_loop(240)
                
    while playing :

        score+=2
        
        screen.fill((255,255,255)) 
        screen.blit(sky,(0,0))
        
        for obj in horizon_1:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        score_string=str(score)
        nb_position=-1
        for n in score_string[1:len(score_string)-2]:
            nb_position+=1
            nb=int(n)
            screen.blit(numbers[nb],(nb_position*35+20,40))
        
        for i in range (0,life_nb):
            screen.blit(life,(900-i*100,40))
            
        for obj in horizon_2:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        for obj in horizon_3:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        for obj in horizon_4:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
            
        for obj in horizon_5:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        for obj in horizon_7:
            obj.pose_update()
            
            if cool_down<200 and cool_down%2==0:
                screen.blit(obj.image,(obj.pose_x,obj.pose_y))
            elif cool_down>200:
                screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        for obj in horizon_6:
            obj.recycle()
            obj.pose_update()
            screen.blit(obj.image,(obj.pose_x,obj.pose_y))
        
        if cool_down<201:
                cool_down+=1
        
        if colision()==True and cool_down>200:
            life_nb-=1
            cool_down=0
            if life_nb==0:
                playing=False
    
     
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                playing= False
                menu=False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                horizon_7[0].jump_start()
                
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                playing=False
            
                          
        pygame.display.flip()
        clock.tick_busy_loop(240)
    
    best_scores.append(score)
    best_scores.sort(reverse=True)
    best_scores=best_scores[0:4]
    
    pygame.display.flip()
    clock.tick_busy_loop(240)
    
save()
pygame.quit()