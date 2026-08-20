import pygame

class TextBlock:
    text: int
    text_rect: object
    text_surface: object
    backgroundImage: object
    pos: tuple[int]
    size: tuple[int]
    screen: object
    imageRect: object
    
    def __init__(self,backgroundImage, Text, pos: tuple[int], size: tuple[int],screen) -> None:
            self.screen = screen
            self.text = Text
            self.pos = pos
            self.size = size
            self.backgroundImage = pygame.transform.scale(backgroundImage, self.size)
            self.imageRect = self.backgroundImage.get_rect()
            font = pygame.font.SysFont("Arial", 40)
            self.text_surface = font.render(self.text, True, (255, 255, 255))
    
            # self.text_surface = pygame.transform.scale(text_surface, self.size)
            self.text_rect = self.text_surface.get_rect(center=(pos[0] + self.size[0] / 2, pos[1] + self.size[1] / 2))

    def show(self) -> None:
            self.screen.blit(self.backgroundImage,self.pos)
            self.screen.blit(self.text_surface,self.text_rect)