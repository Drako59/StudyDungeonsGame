import button
from consts import *
from menu_main import *
from dungeon import Dungeon
from dungeon_enum import Subject
import story_screen

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

game_quit = False

#define fonts
font = pygame.font.SysFont("Arial", 20)

#Load dynamic screen sizes.
screen_size = screen.get_size() # (width: int, height: int)
block_size = [x // 100 for x in screen_size]

#load background image
background_image_load = pygame.image.load("Images/dungeons/background.jpg").convert_alpha()
background_image = pygame.transform.scale(background_image_load, (screen_size[0], screen_size[1]))

#load button images
english_dungeon_background = pygame.image.load(ENGLISH_BACKGROUND).convert_alpha()
history_dungeon_background = pygame.image.load(HISTORY_BACKGROUND).convert_alpha()
math_dungeon_background = pygame.image.load(MATH_BACKGROUND).convert_alpha()
science_dungeon_background = pygame.image.load(SCIENCE_BACKGROUND).convert_alpha()

#load block image
block_image_load = pygame.image.load(BLOCK_IMAGE).convert_alpha()
start_block_image_load = pygame.image.load(START_BLOCK_IMAGE).convert_alpha()
end_block_image_load = pygame.image.load(END_BLOCK_IMAGE).convert_alpha()

#load button images
english_dungeon = pygame.image.load("Images/dungeons/english_dungeon.png").convert_alpha()
history_dungeon = pygame.image.load("Images/dungeons/history_dungeon.png").convert_alpha()
math_dungeon = pygame.image.load("Images/dungeons/math_dungeon.png").convert_alpha()
science_dungeon = pygame.image.load("Images/dungeons/science_dungeon.png").convert_alpha()



#create button instances
english_dungeon_button = button.Button(block_size[0] * 15, block_size[1] * 20, english_dungeon, 2)
history_dungeon_button = button.Button(block_size[0] * 15, block_size[1] * 60, history_dungeon, 2)
math_dungeon_button = button.Button(block_size[0] * 55, block_size[1] * 20, math_dungeon, 2)
science_dungeon_button = button.Button(block_size[0] * 55, block_size[1] * 60, science_dungeon, 2)



def choose_dugneon_screen() -> None:
    english_dungeon_button.draw(screen)
    history_dungeon_button.draw(screen)
    math_dungeon_button.draw(screen)
    science_dungeon_button.draw(screen)

def main() -> None:
    status = 0
    run = True

    story_screen.create_welcome_screen()

    while run:
        screen.blit(background_image, (0, 0))
        choose_dugneon_screen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
            if event.type == pygame.QUIT:
                run = False

            if english_dungeon_button.check_click():
                dungeon = Dungeon(english_dungeon_background,start_block_image_load,end_block_image_load,block_image_load, Subject.English, screen,clock)
                screen.blit(background_image, (0,0))

                dungeon.start()

            if history_dungeon_button.check_click():

                screen.blit(background_image, (0,0))
                dungeon = Dungeon(history_dungeon_background,start_block_image_load,end_block_image_load,block_image_load, Subject.History, screen,clock)
                dungeon.start()

            if  math_dungeon_button.check_click():
                screen.blit(background_image, (0,0))
                dungeon = Dungeon(math_dungeon_background,start_block_image_load,end_block_image_load,block_image_load, Subject.Math, screen,clock)
                dungeon.start()

            if science_dungeon_button.check_click():
                screen.blit(background_image, (0,0))
                dungeon = Dungeon(science_dungeon_background,start_block_image_load,end_block_image_load,block_image_load, Subject.Science, screen,clock)
                dungeon.start()
            
        pygame.display.flip()
        clock.tick(400)

    pygame.quit()


if __name__ == '__main__':
    main()