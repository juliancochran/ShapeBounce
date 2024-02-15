'''
Circle class for drawing in Pygame
'''
__author__ = "Julian C"
__version__ = "2.13.2024"

import random
import pygame

class Circle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, radius, screen):
        super().__init__()
        self.image = pygame.Surface([radius, radius])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # screen boundaries
        self.left_boundary = radius
        self.right_boundary = screen.get_width() - radius
        self.top_boundary = radius
        self.bottom_boundary = screen.get_height() - radius
        # random movement of this sprite is here
        self.x_change = random.randint(-5,5)
        self.y_change = random.randint(-5,5)

    '''
    def contains(self, click):
        return super(Circle, self).collidepoint(click)
    '''
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect, self.radius)

    def update(self):
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        # bounce x-axis
        if self.rect.x < self.left_boundary or self.rect.x > self.right_boundary:
            self.x_change *= -1
            #self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        #bounce y-axis
        if self.rect.y < self.top_boundary or self.rect.y > self.bottom_boundary:
            self.y_change *= -1
            #self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        #pygame.draw.circle(screen, self.color, self.rect, self.radius)