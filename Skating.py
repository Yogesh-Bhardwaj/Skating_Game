import pygame
import os
import random


pygame.init()
W = 1300
H = 655
gameWindow = pygame.display.set_mode((W, H))
pygame.display.set_caption("Skating")

bgimg = pygame.image.load("Components/rungame.jpg").convert_alpha()
bgimg = pygame.transform.scale(bgimg, (W, H)).convert_alpha()


runner = pygame.image.load("Components/runner.png").convert_alpha()
_h = runner.get_height()
_w = runner.get_width()
skater = pygame.image.load("Components/skater.png").convert_alpha()
skater = pygame.transform.scale(skater, (_w, _h)).convert_alpha()

skater = pygame.transform.rotozoom(skater, -25, 0.05)
gaddha = pygame.image.load("Components/Gaddha.jpg").convert_alpha()
gaddha = pygame.transform.scale(
gaddha, (int(gaddha.get_width()*(2)), int((3)*H/(16.5)))).convert_alpha()
pygame.display.set_icon(skater)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, int(H/10))


red = (255, 0, 0)
black = (0, 0, 0)


h = skater.get_height()
w = skater.get_width()
gh = gaddha.get_height()
gw = gaddha.get_width()
x = 18

musicc = pygame.mixer.music.load("Sounds/Kalimba.mp3")
crossed = pygame.mixer.Sound("Sounds/Win.wav")
miss = pygame.mixer.Sound("Sounds/lose.wav")
falling = pygame.mixer.Sound("Sounds/falling.wav")


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def welcome():
    gameexit = False
    while not gameexit:
        gameWindow.blit(bgimg, (0, 0))
        gameWindow.blit(skater, (int(W/10), int((13.5)*H/(16.5))-h+x))
        text_screen("Welcome to Skating", black, W/3, H/2)
        text_screen("Press Space Bar To Play", black, W/3, H/2 + H/15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        pygame.display.update()
        clock.tick(60)


fps = 30


def game():
    pygame.mixer.music.play(-1)
    gameexit = False
    gameover = False

    rx = int(W/10)

    ry = int((13.5)*H/(16.5))-h + x
    sx = 0
    vx = -15
    vy = 0
    ay = 0
    g = int(W/3)
    gx1 = int(W)
    gx2 = int(W)+g
    gy = int((13.5)*H/(16.5))-2
    score = 0
    vjump = 30
    gravity = 3
    i = 1
    p = 1
    while not gameexit:
        gameWindow.blit(bgimg, (sx, 0))
        gameWindow.blit(bgimg, (sx-W, 0))
        gameWindow.blit(gaddha, (gx1, gy))
        gameWindow.blit(gaddha, (gx2, gy))

        if(not gameover):

            if(score > 10*i):
                vx = vx-3*(i)
                i += 1
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    gameexit = True

            gameWindow.blit(skater, (rx, ry))
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_SPACE]) and (p):

                if(ry == int((13.5)*H/(16.5))-h + x):
                    vy = vjump
                    ay = gravity

            sx = (sx+vx) % W
            gx1 = (gx1+vx)
            t = 0
            if(gx1 < -gw):
                gx1 = random.randint(W, int(W/2) + W)
                score += 1
                pygame.mixer.Sound.play(crossed)
            gx2 = (gx2+vx)
            if(gx2 < -gw):

                t = 1
                score += 1
                pygame.mixer.Sound.play(crossed)

            if(t):
                g = random.randint(int(W/4), int(W/2))
                gx2 = gx1+g

            ry -= vy/2
            vy -= ay/2
            if(ry == int((13.5)*H/(16.5))-h + x):
                vy = 0
                ay = 0
            if((gx1 >= rx+int(w/2)-gw) and (gx1 <= rx+int(w/2))) and (ry == int((13.5)*H/(16.5))-h + x):

                vx = 0
                ay = 3
                p = 0
                pygame.mixer.Sound.play(miss)
            if((gx2 >= rx+int(w/2)-gw) and (gx2 <= rx+int(w/2))) and (ry == int((13.5)*H/(16.5))-h + x):

                vx = 0
                ay = 3
                p = 0
                pygame.mixer.Sound.play(miss)

            ry -= vy/2
            vy -= ay/2
            if(ry > H+x):

                gameover = True
            text_screen("Score: " + str(score), red, 5, 5)
        else:
            pygame.mixer.music.pause()
            gameWindow.blit(bgimg, (0, 0))
            text_screen(f"SCORE = {score}", red, W/10, H/2)
            text_screen("Game Over! Press Enter To Continue",
                        red, W/40, H/2 + H/15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
