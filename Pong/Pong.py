import pygame, time, random, sys


class ball(pygame.sprite.Sprite):
    x, y, offset, lives = 0, 0, [1, 1], 5
    def __init__(self, sx, sy):
        pygame.sprite.Sprite.__init__(self)
        self.x = sx
        self.y = sy
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 0), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (sx, sy)
        offset = [1, 1]
    def update(self):
        self.x += self.offset[0]
        self.y += self.offset[1]
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.offset[0] *= -1
        elif self.rect.top <= 5:
            self.offset[1] *= -1
        if self.rect.bottom >= screen.get_height()-5:
            if self.lives != 0:
                self.lives -= 1
                self.bounce()
            else:
                return 0
        return 1
    def bounce(self):
        self.offset[1] *= -1

class board(pygame.sprite.Sprite):
    x = 0
    y = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = screen.get_height()-60
        self.image = pygame.Surface([100, 20])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def update(self, spot):
        self.rect.x = spot[0]-50

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Pong")
img = pygame.image.load("Pong.png")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 30)
while 1:
    screen.blit(img, (0, 0))
    screen.blit(font.render("Press any key to continue...",1, (255, 255, 255)), (0, 570))
    flag = 1
    pygame.display.update()
    score = 0
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                flag = 0
    st = time.time()
    flag = 1
    bx = random.randint(10, 790)
    by = random.randint(10, 200)
    group = pygame.sprite.Group()
    ball1 = ball(bx, by)
    group.add(ball1)
    board1 = board()
    group.add(board1)
    i = 0
    while flag:
        clock.tick(400)
        screen.fill((0, 0, 0))
        screen.blit(font.render("Lives:%d Score:%d Time:%d s" %(ball1.lives,score,time.time()-st), 1, (255, 255, 255)), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                spot = pygame.mouse.get_pos()
                board1.update(spot)
        if not ball1.update():
            flag = 0
        if pygame.sprite.collide_rect(ball1, board1):
            ball1.bounce()
            while pygame.sprite.collide_rect(ball1, board1):
                ball1.update()
                clock.tick(200)
            score += 1;
        group.draw(screen)
        pygame.display.update()
        i += 1
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 30), 0)
    screen.blit(font.render("Game Over.Score:%d Time:%d s" %(score,time.time()-st), 1, (255, 255, 255)), (0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (540, 0, 180, 50), 0)
    screen.blit(font.render("Play again", 1, (255, 255, 255)), [544, 10])
    pygame.draw.rect(screen, (0, 0, 255), (720, 0, 80, 50), 0)
    screen.blit(font.render("Quit", 1, (255, 255, 255)), [726, 10])
    flag = 1
    pygame.display.update()
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                spot = pygame.mouse.get_pos();
                if spot[1] <= 50:
                    if spot[0] >= 720:
                        pygame.quit()
                        sys.exit()
                    elif spot[0] >= 540:
                        flag = 0;
    screen.fill((0, 0, 0))
