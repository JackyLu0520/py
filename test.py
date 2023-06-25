import textinput
import pygame


pygame.init()
screen=pygame.display.set_mode([800,600])
s = textinput.textinput(screen, pygame.font.SysFont("Consolas", 30), 30)
print(s)
