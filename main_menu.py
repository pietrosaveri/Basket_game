import pygame 
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


run = True 

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False