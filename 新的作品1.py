import pygame,sys


pygame.init()
screen=pygame.display.set_mode([1366,768],pygame.RESIZABLE)

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)
