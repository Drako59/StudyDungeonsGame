import pygame

from textBlock import TextBlock

class Answer(TextBlock):

    
    isRightAnswer: bool
    
    def __init__(self,backgroundImage, answerText, rightAnswer: bool, pos: tuple[int], size: tuple[int],screen) -> None:
        super().__init__(backgroundImage, answerText, pos, size,screen)

        self.isRightAnswer = rightAnswer


    

    def colideImage(self,pos) -> bool:
        if (self.pos[0] < pos[0] < self.pos[0] + self.size[0]) and (self.pos[1] < pos[1] < self.pos[1] + self.size[1]):
            return True
        return False

    def check_click(self, pos) -> bool:
        if self.colideImage(pos) or self.text_rect.collidepoint(pos) :
                if pygame.mouse.get_pressed()[0] == 1:
                    return True

        return False

