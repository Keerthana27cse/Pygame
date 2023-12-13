import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:
    
    def __init__(self):
         self.width=700
         self.height=700
         self.white_colour=(255,255,255)
         self.game_window=pygame.display.set_mode((self.width,self.height))
         self.clock=pygame.time.Clock()
         self.background=GameObject(0,0,self.width,self.height,'ladder.jpeg')
         self.treasure=GameObject(375,50,50,50,'earth.png')
         self.player=Player(375,550,60,40,'snake.jpg',10)

         self.enemies=[
              Enemy(0,300,60,50,'devil.png',10),#left devil
              Enemy(500,400,60,50,'devil.png',10),#rightdevil
              Enemy(0,200,60,50,'devil.png',10),#left devil
          ]
         self.level=1.0
         
    def reset_map(self):
          self.player=Player(375,550,40,60,'snake.jpg',10) 

          speed=2+(self.level*2)
          if self.level>=4.0:
               self.enemies=[
                     Enemy(0,300,60,50,'devil.png',speed),#left devil
                     Enemy(500,400,60,50,'devil.png',speed),#rightdevil
                     Enemy(0,200,60,50,'devil.png',speed),
               ]
          elif self.level>=2.0:
               self.enemies=[
                     Enemy(0,300,60,50,'devil.png',speed),#left devil
                     Enemy(500,100,60,50,'devil.png',speed),#rightdevil
                     
               ]    
          else:
               self.enemies =[
                     Enemy(0,200,60,50,'devil.png',speed),
               ]

    def draw_objects(self):
         self.game_window.fill(self.white_colour)
         self.game_window.blit(self.background.image,(self.background.x,self.background.y))
         self.game_window.blit(self.treasure.image,(self.treasure.x,self.treasure.y))
         self.game_window.blit(self.player.image,(self.player.x,self.player.y))
         
         for enemy in self.enemies:
             self.game_window.blit(enemy.image,(enemy.x,enemy.y))
         
         pygame.display.update()

    def move_objects(self,player_direction) :   
         self.player.move(player_direction,self.height)  
         for enemy in self. enemies:
             enemy.move(self.width)

    def check_for_collided(self):
          for enemy in self.enemies:
              if self.detect_collision(self.player,enemy):
                  self.level=1.0
                  return True
          if self.detect_collision(self.player,self.treasure):
                  self.level+=0.5
                  return True
          return False

    def detect_collision(self,object_1,object_2):
        #if object_1.y>(object_2.y + object_2.height):
        #    return False
       #elif(object_1.y+object_1.height)<object_2.y:
             #return False
        #if object_1.x>(object_2.x + object_2.width):
          
          #   return False
        #elif(object_1.x+object_1.width)<object_2.x:
           #  return False
        #return True
        if object_1.y<(object_2.y + object_2.height) and (object_1.y+object_1.height)>object_2.y and object_1.x<(object_2.x + object_2.width) and (object_1.x+object_1.width)>object_2.x:
            return True
        return False



    def run_game_loop(self):
        player_direction=0    
        while True:
             events=pygame.event.get()
             for event in events:
                  if event.type==pygame.QUIT:
                      return 
                  elif event.type==pygame.KEYDOWN: 
                       if event.key==pygame.K_UP:
                            player_direction=-1
                       elif event.key==pygame.K_DOWN:
                            player_direction=1
                  elif event.type==pygame.KEYUP:
                        if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                           player_direction=0

             self.move_objects(player_direction)
             self.draw_objects()
             if self.check_for_collided():
                  self.reset_map()
                  



             self.clock.tick(60)

