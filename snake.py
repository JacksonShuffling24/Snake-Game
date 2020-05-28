# Snake Game Spring 2020 v1
# By Swanson, Harpaz, Kumar-Shono, and Stein

import pygame


screen_width = 600
screen_height = 600
snake_size = 10
food_size = 10
snake_color = ((0,0,255))
food_color = ((255,0,0))
snake=[((300,300))]


pygame.init()

# Import pygame.locals to get keystrokes
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

screen = pygame.display.set_mode((screen_width, screen_height))
running = True

while running:

    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False


