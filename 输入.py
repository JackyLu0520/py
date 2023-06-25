import pygame
import textinput


pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption('输入')
font=pygame.font.SysFont('Consolas', 30)
screen.blit(font.render(textinput.textinput \
(screen, font, 30, 100, 100, (255, 255, 255), (0, 0, 0)), 1, (255, 255, 255)),(100, 100))