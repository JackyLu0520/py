import pygame,sys


data = []
n = int(input("个数："))
for i in range(n):
    data.append(int(input()))
Max = int(input("最大值："))
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("柱状图")
screen.fill((255, 255, 255))
pygame.draw.line(screen, (0, 0, 0), (100, 500), (700, 500), 2)
for i in range(500, 100, int(-400/Max)):
    pygame.draw.line(screen, (0, 0, 0), (100, i), (100, i-400/Max), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, i-400/Max), (110, i-400/Max), 2)
j = 0
for i in range(100+int(600/(n+1)), 701-int(600/(n+1)), int(600/(n+1))):
    pygame.draw.rect(screen, (255, 0, 0), \
                     (i-20, 500-400/Max*data[j], 40, 400/Max*data[j]),0)
    j += 1
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
