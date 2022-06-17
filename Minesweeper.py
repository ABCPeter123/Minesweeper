import pygame


# initiating pygame
pygame.init()

#display pygame screen
X = 1200
Y = 900
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Minesweeper')
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

#image loading site
title_image = pygame.image.load("title.png")
title2_image = pygame.image.load("title2.png")
button1 = pygame.image.load("easy_button.png")
button2 = pygame.image.load("medium_button.png")
button3 = pygame.image.load("hard_button.png")

#title class
class title:
    def __init__(self, pos, image, scale = 1):
        width = image.get_width()
        height = image.get_height()
        self.pos = pos
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def show(self):
        screen.blit(self.image, self.rect)

#button class
class button:
    def __init__(self, pos, image, scale = 1):
        width = image.get_width()
        height = image.get_height()
        self.pos = pos
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.clicked = False

    def draw(self):
        action = False
        #detecting whether mouse clicked or not
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, self.rect)

        return action

#button instances
easy_button = button(
    (600, 400),
    button1,
    6
)

medium_button = button(
    (600, 500),
    button2,
    6
)

hard_button = button(
    (600, 600),
    button3,
    6
)

#title instances
main_title = title(
    (600, 150),
    title_image,
    10)

title2 = title(
    (600, 300),
    title2_image,
    5)

#game loop
while True:
    #main menu
    screen.fill("#D3D3D3")
    main_title.show()
    title2.show()
    if easy_button.draw():
        #still under construction
        print('clicked')
    
    if medium_button.draw():
        #still under construction
        print('clicked')
    
    if hard_button.draw():
        #still under construction
        print('clicked')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(30)
    pygame.display.update()