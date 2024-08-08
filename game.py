import pygame
import math
import pyautogui

pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VECTOR_COLOR = (255, 255, 255)
FPS = 60

clock = pygame.time.Clock()
screen_x = 900
screen_y = 500
ball_x = 40
ball_y = 40
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Basketball Game")
BG = pygame.image.load("background.png")
main_font = pygame.font.SysFont("Helvetica", 38, bold = False, italic = True)


jumping = False
X_POSITION = 400
Y_POSITION = 375
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

VEL_BALL = 15
ARROW_X = 500
ARROW_Y = 300
LENGHT_FORCE = 49

ANGLE = 0

count = 0

ball = pygame.image.load("ball.svg.png")
ball = pygame.transform.scale(ball, (80, 80))
ball_rect = ball.get_rect(center = (X_POSITION, Y_POSITION))
ballrect = ball.get_rect()
ball_width = ball.get_width()


class Basket():
    def __init__(self, BASKET_POS_X, BASKET_POS_Y):
        self.image = pygame.image.load("bin.png")
        self.image_x = 170
        self.image_y = 170
        self.image = pygame.transform.scale(self.image, (self.image_x, self.image_y))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (BASKET_POS_X-30, BASKET_POS_Y-70)
        self.rect = self.rect.inflate(-70, -150)

    def draw(self, screen):
        screen.blit(self.image, (BASKET_POS_X, BASKET_POS_Y))
            

BASKET_POS_X = screen_x -150
BASKET_POS_Y = 352 - 90
basket = Basket(BASKET_POS_X, BASKET_POS_Y)


run = True
while run:
    VECTOR_STARTPOINT = pygame.math.Vector2(X_POSITION, Y_POSITION)
    VECTOR_ENDPOINT = pygame.math.Vector2(100, 100)
    CURRENT_ENDPOINT = VECTOR_STARTPOINT + VECTOR_ENDPOINT.rotate(ANGLE)

    POS = (500, 475-100)

    line2 = pygame.draw.line(screen, (0, 0, 0), (VECTOR_STARTPOINT), (POS), 5)
    line = pygame.draw.line(screen, (0, 0, 0), (CURRENT_ENDPOINT), (POS), 5)
    MID_LINE = pygame.draw.line(screen, (0, 0, 0), (VECTOR_STARTPOINT), (VECTOR_STARTPOINT[0], 0))
    GROUND = pygame.draw.line(screen, WHITE, (0, 417), (screen_x, 417), 2)


    #screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys_pressed = pygame.key.get_pressed()

    #if keys_pressed[pygame.K_SPACE]:
        #jumping = True
    #if keys_pressed[pygame.K_d] and X_POSITION < screen_x-ball_width//2:
        #X_POSITION += VEL_BALL
    #if keys_pressed[pygame.K_a] and X_POSITION > 0 + ball_width//2:
        #X_POSITION -= VEL_BALL

    screen.fill(BLACK)
    screen.blit(BG, (0, 0))
    basket.draw(screen)

    #draw force line, red below, white above
    FORCE_MAX = pygame.draw.line(screen, (255, 0, 0) , (400, 50), (50, 50), 5)
    FORCE = pygame.draw.line(screen, WHITE , (LENGHT_FORCE, 50), (50, 50), 5)


    if keys_pressed[pygame.K_r] and LENGHT_FORCE <= 400:
        LENGHT_FORCE += 5

        #coould do it with no hard coding
        if LENGHT_FORCE <= 200 and LENGHT_FORCE > 99:
            #print("low")
            JUMP_HEIGHT = 20
            Y_VELOCITY = JUMP_HEIGHT

        if LENGHT_FORCE > 200 and LENGHT_FORCE < 300:
            #print("medium")
            JUMP_HEIGHT = 25
            Y_VELOCITY = JUMP_HEIGHT

        if LENGHT_FORCE >= 300 and LENGHT_FORCE < 400:
            #print("strong")
            JUMP_HEIGHT = 27
            Y_VELOCITY = JUMP_HEIGHT

        if LENGHT_FORCE == 399:
            #print("maximum")
            JUMP_HEIGHT = 30
            Y_VELOCITY = JUMP_HEIGHT

    #start moving vector
    if Y_POSITION == 375:
        if keys_pressed[pygame.K_w]:
            #VECTOR_COLOR = (255, 255, 255)
    
            ANGLE = (ANGLE + 3) % 360
            LENGHT_VECTOR3 = 141
            LENGHT_GROUND = 417
            VECTOR_LINE = pygame.draw.line(screen, VECTOR_COLOR, VECTOR_STARTPOINT, CURRENT_ENDPOINT, 4)
            LENGHT_CATETUS_MINOR =(CURRENT_ENDPOINT[1]-POS[1])

            try:
                angle = math.asin(LENGHT_CATETUS_MINOR/LENGHT_VECTOR3)

            except:
                pass

            VEL_X = (Y_VELOCITY-15)*math.cos(angle)
            
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                count +=1

                if angle > 0:
                    #print("down")
                    jumping = False

                if angle < 0:
                    #print("Up") 
                    jumping = True
                    pyautogui.press('h')
        if event.type == pygame.QUIT:
            run = False
    

    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY

        if CURRENT_ENDPOINT[0] < MID_LINE[0]:
            X_POSITION -= VEL_X

        if CURRENT_ENDPOINT[0] > MID_LINE[0]:
            X_POSITION +=VEL_X

        #X_POSITION += VEL_X
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT

        if X_POSITION <= 0 + ball_width//2:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
            Y_POSITION = 375
            
        if X_POSITION >= screen_x - ball_width//2:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
            Y_POSITION = 375

        ball_rect = ball.get_rect(center = (X_POSITION, Y_POSITION))
        screen.blit(ball, ball_rect)

    else:
        ball_rect = ball.get_rect(center = (X_POSITION, Y_POSITION))
        screen.blit(ball, ball_rect)

    #collisions


    #pygame.draw.rect(screen, (255, 0, 0), basket.rect, 1)
    #pygame.draw.rect(screen, (255, 0, 0), ball_rect, 1)

    bouce_label = main_font.render("Bounces: " +str(count), 1, WHITE)
    win_label = main_font.render("VICRORY!", 1, WHITE)
    screen.blit(bouce_label, (0, 0))

    if ball_rect.colliderect(basket.rect):
        print("ciao")
        alpha = 128
        #ball.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        trasparent = (0, 0, 0, 0)
        ball.fill(trasparent)
        run = False 


    pygame.display.flip()
    clock.tick(FPS)

