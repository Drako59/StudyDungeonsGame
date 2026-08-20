import sys
import pygame
import consts
import button


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width = screen.get_width()
height = screen.get_height()

background = pygame.image.load(consts.BACKGROUND_STORY)
button_img = pygame.image.load(consts.CONTINUE_BUTTON)
button_size = (140,70)
button_img = pygame.transform.scale(button_img, button_size)
button_rect = button_img.get_rect()
button_pos = (width - 150, height - 80)
button_rect.topleft = button_pos

# creating button object
continue_button = button.Button(button_pos[0], button_pos[1], button_img, 2)


def create_welcome_screen():
    global background
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))
    print_text()
    create_button()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:  # יציאה בלחיצה על Esc
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.check_click():
                    return
        pygame.display.update()

def print_text():
    font = pygame.font.Font(consts.FONT, 30)
    text = font.render(consts.STORY, True, (255, 216, 77))
    text_rect = text.get_rect()
    text_rect.midtop = (screen.get_width() / 2 + 150, 0)
    screen.blit(text, text_rect)


def create_button():
    screen.blit(button_img, button_rect)