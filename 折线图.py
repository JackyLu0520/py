import pygame,sys


data = []
n = int(input("个数："))
for i in range(n):
    data.append(int(input()))
Max = int(input("最大值："))
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("折线图")
screen.fill((255, 255, 255))
#pygame.draw.line(screen, (0, 0, 0), (100, 500), (700, 500), 2)
for i in range(100, 700, int(600/(n+1))):
    pygame.draw.line(screen, (0, 0, 0), (i, 500), (i+600/(n+1), 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (i+600/(n+1), 500),
                     (i+600/(n+1), 490), 2)
for i in range(500, 100, int(-400/Max)):
    pygame.draw.line(screen, (0, 0, 0), (100, i), (100, i-400/Max), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, i-400/Max), (110, i-400/Max), 2)
j = 0
for i in range(100+int(600/(n+1)), 701-int(2*600/(n+1)), int(600/(n+1))):
    pygame.draw.aaline(screen, (255, 0, 0), \
                     (i, int(500-400/Max*data[j])), (i+int(600/(n+1)), int(500-400/Max*data[j+1])), 2)
    pygame.draw.circle(screen, (255, 0, 0), (i, int(500-400/Max*data[j])), 5)
    pygame.draw.circle(screen, (255, 0, 0), \
                       (i+int(600/(n+1)), int(500-400/Max*data[j+1])), 5)
    j += 1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
