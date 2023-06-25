import pygame
import random


pygame.init()
screen = pygame.display.set_mode([1366,768])
pygame.display.set_caption("")
uf = True
while uf:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            uf = False
    pygame.draw.rect(screen, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (random.randint(1, 1366), random.randint(1, 768), random.randint(1, 255), random.randint(1, 255)),0)
    pygame.draw.circle(screen, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (random.randint(1, 1366), random.randint(1, 768)), random.randint(1,100))
    pygame.display.update()
pygame.quit()
