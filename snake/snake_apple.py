import pygame
from random import randint
from constants import *

class Snake:
    def __init__(self):
        self.body = [[5, 10], [6, 10]]
        self.direction = "right"

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def move(self):
        head_x, head_y = self.body[-1]
        if self.direction == 'up': head_y -= 1
        elif self.direction == 'down': head_y += 1
        elif self.direction == 'left': head_x -= 1
        elif self.direction == 'right': head_x += 1
        
        self.body.append([head_x, head_y])
        self.body.pop(0)

    def grow(self):
        self.body.insert(0, list(self.body[0]))

class Apple:
    def __init__(self):
        self.randomize()

    def randomize(self):
        self.pos = [randint(0, GRID_COUNT - 1), randint(0, GRID_COUNT - 1)]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.pos[0] * GRID_SIZE, self.pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))