'''
Using Pygame to learn about classes/objects
OOD and OOP
'''
__author__ = "Julian C"
__version__ = "02.13.2024"

import pygame
from Circle import *

pygame.init()
screen = pygame.display.set_mode((1000,700))
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
# create a heck-tonna circles here
circle_sprites = pygame.sprite.Group()
for i in range(40):
    rancolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    ran_x = random.randint(50,screen.get_width()-50)
    ran_y = random.randint(50,screen.get_height()-50)
    ran_radius = random.randint(20, 50)
    circle_sprites.add(Circle(rancolor, ran_x, ran_y, ran_radius, screen))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        '''if event.type == pygame.MOUSEBUTTONDOWN:
            for circle in reversed(circles):
                if circle.contains(pygame.mouse.get_pos()):
                    circles.remove(circle)'''
    screen.fill(BLACK)
    circle_sprites.draw(screen)
    circle_sprites.update()
    pygame.display.flip()
    clock.tick(120)
