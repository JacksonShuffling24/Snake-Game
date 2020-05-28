# Snake Game Spring 2020 v1
# By Swanson, Harpaz, Kumar-Shono, and Stein

import pygame
from random import randint


screen_width = 600
screen_height = 600

snake_size = 10
food_size = 10

board_width = int(screen_width / snake_size)
board_height = int(screen_height / snake_size)

snake_color = ((0,0,255))
food_color = ((255,0,0))
snake=[(int(board_width/2),int(board_height/2))]
score = 0

#Direction of the snake where 0=left, 1=up, 2=right, 3=down
snake_dir = 0

food_pos = (randint(0, board_width), randint(0, board_height))

pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

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
            elif event.key == K_LEFT:
                snake_dir = 0
            elif event.key == K_UP:
                snake_dir = 1
            elif event.key == K_RIGHT:
                snake_dir = 2
            elif event.key == K_DOWN:
                snake_dir = 3
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    #Modify snake and food

    current_head = snake[0]
    if snake_dir == 0:
        new_head = (current_head[0] - 1, current_head[1])
    if snake_dir == 1:
        new_head = (current_head[0], current_head[1] - 1)
    if snake_dir == 2:
        new_head = (current_head[0] + 1, current_head[1])
    if snake_dir == 3:
        new_head = (current_head[0] - 1, current_head[1])

    if current_head == food_pos:
        score = score + 1
        snake.insert(0, new_head)

    else:
        snake[0] = new_head

    #Draw snake and food

    #Draw Food
    pygame.draw.rect(screen, (255, 0, 0), (snake_size*food_pos[0],snake_size*food_pos[1], snake_size, snake_size))

    #Draw Snake
    for i in range(0,len(snake)):
        segment = snake[i]
        print(segment[0])
        print(segment[1])
        pygame.draw.rect(screen, (0,255,0), (snake_size * segment[0], snake_size * segment[1], snake_size, snake_size))

    pygame.display.flip()

    # Ensure program maintains a rate of 1 frame per second (needs to be modified to speed up!)
    clock.tick(1)
