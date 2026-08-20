import pygame

class Player:
    __ix: int  = 0 #x placment by matrix index
    __iy: int = 0 #y placment by matrix index
    
    __x: int = 0 #raw x placment
    __y: int = 0 #raw y placment

    __step_dx: int = 0 #raw step on x axis distance 
    __step_dy: int = 0 #raw step on y axis distance

    __playerSizes: tuple[int] = (10,10)

    def __init__(self, playerImage,playerSizes: tuple[int], step_dx, step_dy, screen) -> None:
        self.__playerSizes = playerSizes
        self.playerImage = pygame.transform.scale(playerImage, self.__playerSizes)
        self.__step_dx = step_dx
        self.__step_dy = step_dy
        self.__x = 0
        self.__y = 0
        self.__iy = 0
        self.__ix = 0
        self.screen = screen


    def move(self,ix,iy) -> None:
        self.__ix = ix
        self.__iy = iy
        self.__x = self.__ix * self.__step_dx
        self.__y = self.__iy * self.__step_dy
        

    def up(self) -> None:
        self.__y -= self.__step_dy
        self.__iy -= 1


    def down(self) -> None:
        self.__y += self.__step_dy
        self.__iy += 1


    def right(self) -> None:
        self.__x += self.__step_dx
        self.__ix += 1
        
    def left(self) -> None:
        self.__x -= self.__step_dx
        self.__ix -= 1

    def show(self) -> None:
        self.screen.blit(self.playerImage, (self.__x,self.__y))

    def betweenX(self, start, end) -> bool:
        if (start  <= self.__ix < end): 
            return True
        return False

    def betweenY(self, start, end):
        if (start  <= self.__iy < end):
            return True

        return False 

    def getIndexCords(self) -> tuple[int]:
        return (self.__ix, self.__iy)


