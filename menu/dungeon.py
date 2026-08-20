import pygame
from player import Player
from enemy import Enemy
from consts import *
import random as rnd
import time
from env import API_KEY
class Dungeon: 

    
    enemysMatrix: list[list[object]] 

    mazeSize = (20,20)
    # LEVEL 1 - EASY
    __maze1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0],
    [2,1,0,1,1,1,1,1,1,4,1,1,1,1,0,1,1,1,0,0],
    [0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0],
    [0,4,0,1,0,1,1,4,1,1,1,1,0,1,1,1,1,4,0,0],
    [0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,1,1,4,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0],
    [0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,1,1,1,4,1,0,1,1,4,1,1,0,0],
    [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,1,4,1,0,1,1,1,1,1,4,1,0,1,1,1,4,1,0,0],
    [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,1,4,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0],
    [0,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


    __maze2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,1,1,4,0,1,1,1,4,1,1,1,0,1,1,4,1,1,0,0],
    [0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0],
    [0,1,1,1,0,4,0,1,0,1,0,1,0,1,1,1,0,4,0,0],
    [0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0],
    [0,1,0,1,4,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0],
    [0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0],
    [0,1,0,1,0,1,1,4,0,1,0,1,1,1,0,1,0,1,0,0],
    [0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0],
    [0,1,1,1,1,1,0,1,1,4,1,1,0,1,0,1,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0],
    [0,1,1,4,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0],
    [0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,1,0,1,1,1,0,1,0,1,1,1,1,4,1,1,0,1,0,0],
    [0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,1,0,1,0,1,1,1,1,4,1,1,0,1,1,1,0,0],
    [0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
    [0,1,1,1,1,4,1,1,1,1,1,1,0,1,1,1,4,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0]
]


    __maze3 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,1,4,1,1,1,1,1,0,1,1,4,1,1,1,1,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0],
    [0,1,1,4,1,1,0,1,0,1,0,1,1,1,0,1,0,4,0,0],
    [0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,4,1,1,0,1,0,1,0,1,0,1,0,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0],
    [0,1,1,1,0,1,1,1,0,1,4,1,1,1,0,1,0,1,0,0],
    [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0],
    [0,1,4,1,0,1,0,1,1,1,1,1,4,1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,1,1,4,0,1,0,1,0,1,0,1,0,0],
    [0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0],
    [0,1,1,1,0,4,1,1,0,1,0,1,1,1,0,1,0,1,0,0],
    [0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
    [0,1,0,1,4,1,0,1,1,1,1,4,1,1,0,1,1,1,0,0],
    [0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,1,4,1,1,1,0,1,1,4,1,1,1,1,4,1,1,1,1,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


    __maze4 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,1,0,1,4,1,1,1,1,4,0,1,1,1,4,1,0,1,0,0],
    [0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0],
    [0,1,0,1,1,4,1,1,0,1,1,1,0,1,0,1,0,4,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0],
    [0,1,0,4,1,1,0,1,1,4,1,1,1,1,0,1,1,1,0,0],
    [0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,1,1,1,0,1,1,4,1,1,0,1,0,1,1,4,1,1,0,0],
    [0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0],
    [0,1,0,1,1,1,0,1,4,1,0,1,0,1,1,1,4,1,0,0],
    [0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,1,4,1,0,1,1,1,0,1,0,4,1,1,1,1,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0],
    [0,1,0,1,1,4,1,1,0,1,1,1,0,1,0,1,0,4,0,0],
    [0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0],
    [0,1,0,1,0,4,0,1,0,1,1,4,0,1,0,1,1,1,0,0],
    [0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],
    [0,1,1,4,1,1,0,1,1,1,4,1,1,1,1,4,1,1,1,3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

    def __init__(self, backImage, startBlockImage, endBlockImage,blockImage, Type, screen, clock):
        self.clock = clock
        self.screen = screen
        self.screenSizes = self.screen.get_size()
        self.blockWidth = self.screenSizes[0] / self.mazeSize[0]
        self.blockHeight = self.screenSizes[1] / self.mazeSize[1]
        self.backImage = pygame.transform.scale(backImage, self.screenSizes)
        self.blockImage = pygame.transform.scale(blockImage, (self.blockWidth,self.blockHeight))
        self.backImageLoad = backImage
        self.endBlockImage = pygame.transform.scale(endBlockImage, (self.blockWidth,self.blockHeight))
        self.startBlockImage = pygame.transform.scale(startBlockImage, (self.blockWidth,self.blockHeight))

        playerImage = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.player = Player(playerImage, (self.blockWidth,self.blockHeight) ,self.blockWidth,self.blockHeight,self.screen)



        self.enemysMatrix = [[None for _ in range(20)]  for _ in range(20)]
        self.currentLevel = 1


        self.lostImage = pygame.image.load(LOST_IMAGE).convert_alpha()
        self.lostImage = pygame.transform.scale(self.lostImage, (self.screenSizes))
        self.wonImage = pygame.image.load(WON_IMAGE).convert_alpha()
        self.wonImage = pygame.transform.scale(self.wonImage, (self.screenSizes))
 
    def show_maze(self, maze: list[list[int]]) -> None:
        
        for row in range( len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == 0:
                    self.screen.blit(self.blockImage, (self.blockWidth * col, self.blockHeight * row))
                elif maze[row][col] == 4 and self.enemysMatrix[row][col] != None:
                    enemy: Enemy = self.enemysMatrix[row][col]
                    enemy.show()
                elif maze[row][col] == 3:
                    self.screen.blit(self.endBlockImage, (self.blockWidth * col, self.blockHeight * row))
                elif maze[row][col] == 2:
                    self.screen.blit(self.startBlockImage, (self.blockWidth * col, self.blockHeight * row))


    

    def load_enemys(self,maze) -> None:
        test_question = "What is your name?"
        test_answers = ["ofri","itamar", "talya", "eliran"]
        for row in range( len(maze)):
            for col in range(len(maze[0])):
                
                if maze[row][col] == 4:
                    # new_background_enemy_image = pygame.image.load(ENEMY_BACKGROUND).convert_alpha()
                    new_background_enemy_image = self.backImageLoad
                    new_enemy_image = pygame.image.load(rnd.choice(ENEMYS_IMAGES)).convert_alpha()
                    new_enemy = Enemy( new_background_enemy_image,new_enemy_image, self.blockWidth * col, self.blockHeight * row,
                                       (self.blockWidth,self.blockHeight), self.screen, self.clock,test_question , test_answers, test_answers[0] )
                    self.enemysMatrix[row][col] = new_enemy 

    def counter_enemy(self,maze,pos: tuple[int]) -> bool:

        if  maze[pos[1]][pos[0]] == 4 and self.enemysMatrix[pos[1]][pos[0]] != None:
            enemy: Enemy =  self.enemysMatrix[pos[1]][pos[0]]
            status = enemy.ShowDialogQuestion()
            if status == True:
                self.enemysMatrix[pos[1]][pos[0]] = None
            return status

        return True

    def check_pass_level(self,maze,pos):
        if  maze[pos[1]][pos[0]] == 3:
            return True

        return False


    def start(self):



        maze: list[list[int]]

        match self.currentLevel:
            case 1:
                maze = self.__maze1
            case 2:
                maze = self.__maze2
            case 3:
                maze = self.__maze3
            case 4:
                maze = self.__maze4
            case _:
                self.show_won_screen()
                return

        self.player.down()

        playerCords = self.player.getIndexCords() # (ix , iy)
        
        self.load_enemys(maze)
        run = True
        while run:
            moved = False
            # print(playerCords)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.event.clear()
                        return
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.event.clear()
                return

            if not moved and (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.player.betweenY(0, self.mazeSize[1] - 1) and maze[playerCords[1] + 1][playerCords[0]] != 0 :
                self.player.down()
                playerCords = self.player.getIndexCords()
                moved = True

            if not moved and (keys[pygame.K_w] or keys[pygame.K_UP]) and self.player.betweenY(1, self.mazeSize[1] - 1) and maze[playerCords[1] - 1][playerCords[0]] != 0:
                self.player.up()
                playerCords = self.player.getIndexCords()
                moved = True

            if not moved and (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.player.betweenX(0, self.mazeSize[0] - 1) and maze[playerCords[1]][playerCords[0] + 1] != 0:
                self.player.right()
                playerCords = self.player.getIndexCords()
                moved = True

            if not moved and (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.player.betweenX(1, self.mazeSize[0] - 1) and maze[playerCords[1]][playerCords[0] - 1] != 0:
                self.player.left()
                playerCords = self.player.getIndexCords()
                moved = True

            if not self.counter_enemy(maze,playerCords):
                pygame.event.clear()
                while pygame.mouse.get_pressed()[0]:
                    pygame.event.pump()
                    self.clock.tick(60)
                self.show_lost_screen()
                return

            if self.check_pass_level(maze,playerCords):
                self.currentLevel += 1
                self.player.move(0,0)
                pygame.display.flip()
                return self.start()

            self.screen.blit(self.backImage, (0,1))
            self.show_maze(maze)
            self.player.show()
            pygame.display.flip()   
            self.clock.tick(8)



    def  show_lost_screen(self) -> None:
        self.screen.blit(self.lostImage, (0,0))
        pygame.display.flip()
        time.sleep(2)

    def  show_won_screen(self) -> None:
        self.screen.blit(self.wonImage, (0,0))
        pygame.display.flip()
        time.sleep(2)

        

    
    




    


        
                    




    






        







