from math import floor
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
exit_image = pygame.image.load("exit.png")
easy_grid_image = pygame.image.load("grid_80_80.png")
medium_grid_image = pygame.image.load("Grid_50_50.png")
hard_grid_image = pygame.image.load("grid_35_35.png")
leave_image = pygame.image.load("leave.png")
easy_grid_0_image = pygame.image.load("0_grid_80_80.png")
medium_grid_0_image = pygame.image.load("0_grid_50_50.png")
hard_grid_0_image = pygame.image.load("0_grid_35_35.png")

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

    def disappear(self):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)

#button class
class button:
    def __init__(self, pos, image, scale = 1, work = True, action = False):
        width = image.get_width()
        height = image.get_height()
        self.pos = pos
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.clicked = False
        self.work = work
        self.action = action

    def draw(self):
        #detecting whether mouse clicked or not
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)

        return self.action
        
    def disappear(self):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)
        self.work = False
        self.action = False

    def make_work(self):
        self.work = True
        
#grid class
class grid:
    def __init__(self, image, pos, status = 'none'):
        self.image = image
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.status = status
    
    def draw(self):
        screen.blit(self.image, self.rect)

    def disappear(self):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)

    def change(self, image):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)
        screen.blit(image, self.rect)

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

exit = button(
    (600, 750),
    exit_image,
    6
)

leave = button(
    (600, 850),
    leave_image,
    4
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

#grid instances
i = 0
n = 0
while n <= 11:
    globals()[f"y{n}"] = 1
    n += 1
n = 0
while i < 108:
    while n <= 11:
        if i % 12 == n:
            globals()[f"easy_grid_{i}"] = grid(easy_grid_image, (80 * (n + 2), 80 * (globals()[f"y{n}"])))
            globals()[f"y{n}"] += 1
        n += 1
    if n == 12:
        n = 0
    i += 1

i = 0
n = 0
while n <= 19:
    globals()[f"y{n}"] = 1
    n += 1
n = 0
while i < 300:
    while n <= 19:
        if i % 20 == n:
            globals()[f"medium_grid_{i}"] = grid(medium_grid_image, (50 * (n + 2) + 25, 50 * (globals()[f"y{n}"] + 1)-50))
            globals()[f"y{n}"] += 1
        n += 1
    if n == 20:
        n = 0
    i += 1

i = 0
n = 0
while n <= 27:
    globals()[f"y{n}"] = 1
    n += 1
n = 0
while i < 588:
    while n <= 27:
        if i % 28 == n:
            globals()[f"hard_grid_{i}"] = grid(hard_grid_image, (35 * (n + 2) + 57.5, 35 * (globals()[f"y{n}"] + 1)))
            globals()[f"y{n}"] += 1
        n += 1
    if n == 28:
        n = 0
    i += 1


loop = True

#game loop
while loop == True:
    #main menu
    screen.fill("#D3D3D3")
    main_title.show()
    title2.show()

    if easy_button.draw() and easy_button.work == True:
        #main menu disappear
        main_title.disappear()
        title2.disappear()
        easy_button.disappear()
        medium_button.disappear()
        hard_button.disappear()
        exit.disappear()

        #display the grids
        i = 0
        while i < 108:
            globals()[f"easy_grid_{i}"].draw() 
            i += 1

        clicked = 0
        action = False

        #game loop for game play
        easy_loop = True
        while easy_loop == True:
            
            #calculating which box player is pressing
            x,y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] == 1 and clicked == 1:
                if 120 <= x <= 1080 and 40 <= y <= 760:
                    n = floor(x / 80 - 0.5) - 1 + floor(y / 80 - 0.5) * 12
                else:
                    n = -1
                clicked += 1
                action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                clicked = 1

            #action 
            if action == True:
                if 0 <= n <= 107:
                    globals()[f'easy_grid_{n}'].change(easy_grid_0_image)
                else:
                    pass

            action = False

            #leave
            if leave.draw():
                easy_loop = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

        #make the game disappear and goes back to the main menu
        i = 0
        while i < 108:
            globals()[f"easy_grid_{i}"].disappear()
            i += 1

        leave.disappear()

        #make the main menu buttons work again
        easy_button.make_work()
        medium_button.make_work()
        hard_button.make_work()
        exit.make_work()
            
        pygame.display.update()
    if medium_button.draw() and medium_button.work == True:
        #main menu disappear
        main_title.disappear()
        title2.disappear()
        easy_button.disappear()
        medium_button.disappear()
        hard_button.disappear()
        exit.disappear()

        #display the grids
        i = 0
        while i < 300:
            globals()[f"medium_grid_{i}"].draw() 
            i += 1

        clicked = 0
        action = False

        #game loop for game play
        medium_loop = True
        while medium_loop == True:
            
            #calculating which box player is pressing
            x,y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] == 1 and clicked == 1:
                if 100 <= x <= 1100 and 25 <= y <= 775:
                    n = floor(x / 50) - 2 + floor(y / 50 - 0.5) * 20
                else:
                    n = -1
                clicked += 1
                action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                clicked = 1

            #action 
            if action == True:
                if 0 <= n <= 299:
                    globals()[f'medium_grid_{n}'].change(medium_grid_0_image)
                else:
                    pass

            action = False

            #leave
            if leave.draw():
                medium_loop = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

        #make the game disappear and goes back to the main menu
        i = 0
        while i < 300:
            globals()[f"medium_grid_{i}"].disappear()
            i += 1

        leave.disappear()

        #make the main menu buttons work again
        easy_button.make_work()
        medium_button.make_work()
        hard_button.make_work()
        exit.make_work() 
            
        pygame.display.update()
    if hard_button.draw() and hard_button.work == True:
        #main menu disappear
        main_title.disappear()
        title2.disappear()
        easy_button.disappear()
        medium_button.disappear()
        hard_button.disappear()
        exit.disappear()

        #display the grids
        i = 0
        while i < 588:
            globals()[f"hard_grid_{i}"].draw() 
            i += 1

        clicked = 0
        action = False

        #game loop for game play
        hard_loop = True
        while hard_loop == True:
            
            #calculating which box player is pressing
            x,y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] == 1 and clicked == 1:
                if 110 <= x <= 1090 and 52.5 <= y <= 787.5:
                    n = floor(x / 35 - 1/7) - 3 + (floor(y / 35 - 0.5) - 1) * 28
                else:
                    n = -1
                clicked += 1
                action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                clicked = 1

            #action 
            if action == True:
                if 0 <= n <= 587:
                    globals()[f'hard_grid_{n}'].change(hard_grid_0_image)
                else:
                    pass

            action = False

            #leave
            if leave.draw():
                hard_loop = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

        #make the game disappear and goes back to the main menu
        i = 0
        while i < 588:
            globals()[f"hard_grid_{i}"].disappear()
            i += 1

        leave.disappear()

        #make the main menu buttons work again
        easy_button.make_work()
        medium_button.make_work()
        hard_button.make_work()
        exit.make_work() 
            
        pygame.display.update()
    
    if exit.draw() and exit.work == True:
        loop = False
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(30)

    pygame.display.update()
        