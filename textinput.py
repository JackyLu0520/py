from pygame import *
from time import *


def textinput(screen, font1, size, sx=0, sy=0, color=(255, 255, 255), screencolor=(0, 0, 0)):
    s = []
    s1 = ''
    x = sx
    y = sy
    while 1:
        if(time() % 2 == 0):
            draw.rect(screen, screencolor, (x, y, size/2, size), 0)
        else:
            screen.blit(font1.render("|", 0, color), (x, y))
        for event1 in event.get():
            if event1.type == KEYDOWN:
                draw.rect(screen, screencolor, (x, y, size/2, size), 0)
                if event1.key == K_1:
                    screen.blit(font1.render("1|", 1, color), (x, y))
                    x += 15
                    s += '1'
                elif event1.key == K_2:
                    screen.blit(font1.render("2|", 1, color), (x, y))
                    x += 15
                    s += '2'
                elif event1.key == K_3:
                    screen.blit(font1.render("3|", 1, color), (x, y))
                    x += 15
                    s += '3'
                elif event1.key == K_4:
                    screen.blit(font1.render("4|", 1, color), (x, y))
                    x += 15
                    s += '4'
                elif event1.key == K_5:
                    screen.blit(font1.render("5|", 1, color), (x, y))
                    x += 15
                    s += '5'
                elif event1.key == K_6:
                    screen.blit(font1.render("6|", 1, color), (x, y))
                    x += 15
                    s += '6'
                elif event1.key == K_7:
                    screen.blit(font1.render("7|", 1, color), (x, y))
                    x += 15
                    s += '7'
                elif event1.key == K_8:
                    screen.blit(font1.render("8|", 1, color), (x, y))
                    x += 15
                    s += '8'
                elif event1.key == K_9:
                    screen.blit(font1.render("9|", 1, color), (x, y))
                    x += 15
                    s += '9'
                elif event1.key == K_0:
                    screen.blit(font1.render("0|", 1, color), (x, y))
                    x += 15
                    s += '0'
                elif event1.key == K_a:
                    screen.blit(font1.render("a|", 1, color), (x, y))
                    x += 15
                    s += 'a'
                elif event1.key == K_b:
                    screen.blit(font1.render("b|", 1, color), (x, y))
                    x += 15
                    s += 'b'
                elif event1.key == K_c:
                    screen.blit(font1.render("c|", 1, color), (x, y))
                    x += 15
                    s += 'c'
                elif event1.key == K_d:
                    screen.blit(font1.render("d|", 1, color), (x, y))
                    x += 15
                    s += 'd'
                elif event1.key == K_e:
                    screen.blit(font1.render("e|", 1, color), (x, y))
                    x += 15
                    s += 'e'
                elif event1.key == K_f:
                    screen.blit(font1.render("f|", 1, color), (x, y))
                    x += 15
                    s += 'f'
                elif event1.key == K_g:
                    screen.blit(font1.render("g|", 1, color), (x, y))
                    x += 15
                    s += 'g'
                elif event1.key == K_h:
                    screen.blit(font1.render("h|", 1, color), (x, y))
                    x += 15
                    s += 'h'
                elif event1.key == K_i:
                    screen.blit(font1.render("i|", 1, color), (x, y))
                    x += 15
                    s += 'i'
                elif event1.key == K_j:
                    screen.blit(font1.render("j|", 1, color), (x, y))
                    x += 15
                    s += 'j'
                elif event1.key == K_k:
                    screen.blit(font1.render("k|", 1, color), (x, y))
                    x += 15
                    s += 'k'
                elif event1.key == K_l:
                    screen.blit(font1.render("l|", 1, color), (x, y))
                    x += 15
                    s += 'l'
                elif event1.key == K_m:
                    screen.blit(font1.render("m|", 1, color), (x, y))
                    x += 15
                    s += 'm'
                elif event1.key == K_n:
                    screen.blit(font1.render("n|", 1, color), (x, y))
                    x += 15
                    s += 'n'
                elif event1.key == K_o:
                    screen.blit(font1.render("o|", 1, color), (x, y))
                    x += 15
                    s += 'o'
                elif event1.key == K_p:
                    screen.blit(font1.render("p|", 1, color), (x, y))
                    x += 15
                    s += 'p'
                elif event1.key == K_q:
                    screen.blit(font1.render("q|", 1, color), (x, y))
                    x += 15
                    s += 'q'
                elif event1.key == K_r:
                    screen.blit(font1.render("r|", 1, color), (x, y))
                    x += 15
                    s += 'r'
                elif event1.key == K_s:
                    screen.blit(font1.render("s|", 1, color), (x, y))
                    x += 15
                    s += 's'
                elif event1.key == K_t:
                    screen.blit(font1.render("t|", 1, color), (x, y))
                    x += 15
                    s += 't'
                elif event1.key == K_u:
                    screen.blit(font1.render("u|", 1, color), (x, y))
                    x += 15
                    s += 'u'
                elif event1.key == K_v:
                    screen.blit(font1.render("v|", 1, color), (x, y))
                    x += 15
                    s += 'v'
                elif event1.key == K_w:
                    screen.blit(font1.render("w|", 1, color), (x, y))
                    x += 15
                    s += 'w'
                elif event1.key == K_x:
                    screen.blit(font1.render("x|", 1, color), (x, y))
                    x += 15
                    s += 'x'
                elif event1.key == K_y:
                    screen.blit(font1.render("y|", 1, color), (x, y))
                    x += 15
                    s += 'y'
                elif event1.key == K_z:
                    screen.blit(font1.render("z|", 1, color), (x, y))
                    x += 15
                    s += 'z'
                elif event1.key == K_BACKSPACE:
                    if x != sx:
                        x -= 15
                        draw.rect(screen, screencolor, (x, y, size/2, size), 0)
                        s.pop()
                    screen.blit(font1.render("|", 1, color), (x, y))
                elif event1.key == K_SPACE:
                    screen.blit(font1.render(" |", 1, color), (x, y))
                    x += 15
                    s += ' '
                elif event1.key == K_RETURN:
                    for i in range(len(s)):
                        s1 += s[i]
                    draw.rect(screen, screencolor,
                              (x, y, size*len(s)/2+size/2, size))
                    return s1
        display.update()


if __name__ == '__main__':
    init()
    screen = display.set_mode([400, 200])
    screen.fill((255, 255, 255))
    font1 = font.SysFont("Consolas", 30)
    print(textinput(screen, font1, 30, 50, 50, (0, 0, 0), (255, 255, 255)))
    quit()
