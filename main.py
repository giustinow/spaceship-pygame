import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
VEL = 5

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

SPACESHIP_HEIGHT = 30
SPACESHIP_WIDTH = 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def handle_yellow_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    elif key_pressed[pygame.K_d] and yellow.x + VEL + 20 < WIDTH:
        yellow.x += VEL
    elif key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:
        yellow.y += VEL
    elif key_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL


def handle_red_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x:
        red.x -= VEL
    elif key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    elif key_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:
        red.y += VEL
    elif key_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL


def main():
    red = pygame.Rect(800, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        handle_yellow_movement(key_pressed, yellow)
        handle_red_movement(key_pressed, red)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == '__main__':
    main()
