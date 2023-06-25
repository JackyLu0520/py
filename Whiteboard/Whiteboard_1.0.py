import pygame


pygame.init()
icon=pygame.image.load("icon.png")
screen = pygame.display.set_mode([1366, 768], pygame.RESIZABLE)
pygame.display.set_icon(icon)
pygame.display.set_caption("Whiteboard 1.0")
radins = 15
mousedown = False
UnFinished = True
white = 255, 255, 255
red = 255, 0, 0
yellow = 255, 255, 0
black = 0, 0, 0
blue = 0, 0, 255
green = 0, 128, 0
purple = 128, 0, 128
cyan = 0, 255, 255
brown = 128, 64, 0
orange = 255, 128, 0
screen.fill(white)
font = pygame.font.SysFont("Consolas", 15)
pygame.draw.rect(screen, black, (0, 0, 50, 50), 0)
screen.blit(font.render("Eraser", 1, white), [1, 18])
pygame.draw.rect(screen, red, (50, 0, 50, 50), 0)
pygame.draw.rect(screen, green, (100, 0, 50, 50), 0)
pygame.draw.rect(screen, yellow, (150, 0, 50, 50), 0)
pygame.draw.rect(screen, blue, (200, 0, 50, 50), 0)
pygame.draw.rect(screen, purple, (250, 0, 50, 50), 0)
pygame.draw.rect(screen, cyan, (300, 0, 50, 50), 0)
pygame.draw.rect(screen, black, (350, 0, 50, 50), 0)
pygame.draw.rect(screen, brown, (400, 0, 50, 50), 0)
pygame.draw.rect(screen, orange, (450, 0, 50, 50), 0)
pygame.draw.circle(screen, black, (575, 25), 15)
pygame.draw.circle(screen, black, (625, 25), 12)
pygame.draw.circle(screen, black, (675, 25), 10)
pygame.draw.circle(screen, black, (725, 25), 7)
pygame.draw.circle(screen, black, (775, 25), 5)
pygame.draw.rect(screen, black, (875, 0, 50, 50), 0)
screen.blit(font.render("Clean", 1, white), [880, 18])
pygame.draw.rect(screen, black, (350, 50, 50, 25), 0)
pygame.draw.rect(screen, black, (550, 50, 50, 25), 0)
color = black
while UnFinished:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            UnFinished = False
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            mousedown = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            mousedown = False
    if mousedown:
        spot = pygame.mouse.get_pos()
        if (spot[0] <= 50 and spot[1] <= 50):
            color = white
            pygame.draw.rect(screen, black, (0, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 0, 25), 0)
            pygame.draw.rect(screen, white, (50, 50, 450, 25), 0)
        elif (spot[0] <= 100 and spot[1] <= 50):
            color = red
            pygame.draw.rect(screen, color, (50, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (100, 50, 400, 25), 0)
        elif (spot[0] <= 150 and spot[1] <= 50):
            color = green
            pygame.draw.rect(screen, color, (100, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 100, 25), 0)
            pygame.draw.rect(screen, white, (150, 50, 350, 25), 0)
        elif (spot[0] <= 200 and spot[1] <= 50):
            color = yellow
            pygame.draw.rect(screen, color, (150, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 150, 25), 0)
            pygame.draw.rect(screen, white, (200, 50, 300, 25), 0)
        elif (spot[0] <= 250 and spot[1] <= 50):
            color = blue
            pygame.draw.rect(screen, color, (200, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 200, 25), 0)
            pygame.draw.rect(screen, white, (250, 50, 250, 25), 0)
        elif (spot[0] <= 300 and spot[1] <= 50):
            color = purple
            pygame.draw.rect(screen, color, (250, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 250, 25), 0)
            pygame.draw.rect(screen, white, (300, 50, 200, 25), 0)
        elif (spot[0] <= 350 and spot[1] <= 50):
            color = cyan
            pygame.draw.rect(screen, color, (300, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 300, 25), 0)
            pygame.draw.rect(screen, white, (350, 50, 150, 25), 0)
        elif (spot[0] <= 400 and spot[1] <= 50):
            color = black
            pygame.draw.rect(screen, color, (350, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 350, 25), 0)
            pygame.draw.rect(screen, white, (400, 50, 100, 25), 0)
        elif (spot[0] <= 450 and spot[1] <= 50):
            color = brown
            pygame.draw.rect(screen, color, (400, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 400, 25), 0)
            pygame.draw.rect(screen, white, (450, 50, 50, 25), 0)
        elif (spot[0] <= 500 and spot[1] <= 50):
            color = orange
            pygame.draw.rect(screen, color, (450, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (0, 50, 450, 25), 0)
            pygame.draw.rect(screen, white, (500, 50, 0, 25), 0)
        elif (spot[0] <= 600 and spot[1] <= 50):
            radins = 15
            pygame.draw.rect(screen, black, (550, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (550, 50, 0, 25), 0)
            pygame.draw.rect(screen, white, (600, 50, 200, 25), 0)
        elif (spot[0] <= 650 and spot[1] <= 50):
            radins = 12
            pygame.draw.rect(screen, black, (600, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (550, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (650, 50, 150, 25), 0)
        elif (spot[0] <= 700 and spot[1] <= 50):
            radins = 10
            pygame.draw.rect(screen, black, (650, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (550, 50, 100, 25), 0)
            pygame.draw.rect(screen, white, (700, 50, 100, 25), 0)
        elif (spot[0] <= 750 and spot[1] <= 50):
            radins = 7
            pygame.draw.rect(screen, black, (700, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (550, 50, 150, 25), 0)
            pygame.draw.rect(screen, white, (750, 50, 50, 25), 0)
        elif (spot[0] <= 800 and spot[1] <= 50):
            radins = 5
            pygame.draw.rect(screen, black, (750, 50, 50, 25), 0)
            pygame.draw.rect(screen, white, (550, 50, 200, 25), 0)
            pygame.draw.rect(screen, white, (800, 50, 0, 25), 0)
        elif(spot[0] <= 925 and spot[1] <= 50):
            pygame.draw.rect(screen, white, (0, 75, 2000, 2000), 0)
        if (spot[1] >= 75):
            pygame.draw.circle(screen, color, spot, radins)
    pygame.display.update()
pygame.quit()
