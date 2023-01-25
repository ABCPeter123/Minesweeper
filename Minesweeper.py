from math import floor
import random
import time
import pygame
import os

# initiating pygame
pygame.init()

#display pygame screen
X = 1200
Y = 900
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Minesweeper')
1
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

#image loading site
dir_path = os.path.dirname(os.path.realpath(__file__))
title_image = pygame.image.load(os.path.join(dir_path, "Sources", "title.png")).convert()
title2_image = pygame.image.load(os.path.join(dir_path, "Sources", "title2.png")).convert()
button1 = pygame.image.load(os.path.join(dir_path, "Sources", "easy_button.png")).convert()
button2 = pygame.image.load(os.path.join(dir_path, "Sources", "medium_button.png")).convert()
button3 = pygame.image.load(os.path.join(dir_path, "Sources", "hard_button.png")).convert()
exit_image = pygame.image.load(os.path.join(dir_path, "Sources", "exit.png")).convert()
easy_grid_image = pygame.image.load(os.path.join(dir_path, "Sources", "grid_80_80.png")).convert()
medium_grid_image = pygame.image.load(os.path.join(dir_path, "Sources", "Grid_50_50.png")).convert()
hard_grid_image = pygame.image.load(os.path.join(dir_path, "Sources", "grid_35_35.png")).convert()
leave_image = pygame.image.load(os.path.join(dir_path, "Sources", "leave.png")).convert()
easy_grid_0_image = pygame.image.load(os.path.join(dir_path, "Sources", "0_grid_80_80.png")).convert()
medium_grid_0_image = pygame.image.load(os.path.join(dir_path, "Sources", "0_grid_50_50.png")).convert()
hard_grid_0_image = pygame.image.load(os.path.join(dir_path, "Sources", "0_grid_35_35.png")).convert()
easy_grid_mine_image = pygame.image.load(os.path.join(dir_path, "Sources", "mine_grid_80_80.png")).convert()
medium_grid_mine_image = pygame.image.load(os.path.join(dir_path, "Sources", "mine_grid_50_50.png")).convert()
hard_grid_mine_image = pygame.image.load(os.path.join(dir_path, "Sources", "mine_grid_35_35.png")).convert()
easy_grid_1_image = pygame.image.load(os.path.join(dir_path, "Sources", "1_grid_80_80.png")).convert()
easy_grid_2_image = pygame.image.load(os.path.join(dir_path, "Sources", "2_grid_80_80.png")).convert()
easy_grid_3_image = pygame.image.load(os.path.join(dir_path, "Sources", "3_grid_80_80.png")).convert()
easy_grid_4_image = pygame.image.load(os.path.join(dir_path, "Sources", "4_grid_80_80.png")).convert()
easy_grid_5_image = pygame.image.load(os.path.join(dir_path, "Sources", "5_grid_80_80.png")).convert()
easy_grid_6_image = pygame.image.load(os.path.join(dir_path, "Sources", "6_grid_80_80.png")).convert()
easy_grid_7_image = pygame.image.load(os.path.join(dir_path, "Sources", "7_grid_80_80.png")).convert()
easy_grid_8_image = pygame.image.load(os.path.join(dir_path, "Sources", "8_grid_80_80.png")).convert()
medium_grid_1_image = pygame.image.load(os.path.join(dir_path, "Sources", "1_grid_50_50.png")).convert()
medium_grid_2_image = pygame.image.load(os.path.join(dir_path, "Sources", "2_grid_50_50.png")).convert()
medium_grid_3_image = pygame.image.load(os.path.join(dir_path, "Sources", "3_grid_50_50.png")).convert()
medium_grid_4_image = pygame.image.load(os.path.join(dir_path, "Sources", "4_grid_50_50.png")).convert()
medium_grid_5_image = pygame.image.load(os.path.join(dir_path, "Sources", "5_grid_50_50.png")).convert()
medium_grid_6_image = pygame.image.load(os.path.join(dir_path, "Sources", "6_grid_50_50.png")).convert()
medium_grid_7_image = pygame.image.load(os.path.join(dir_path, "Sources", "7_grid_50_50.png")).convert()
medium_grid_8_image = pygame.image.load(os.path.join(dir_path, "Sources", "8_grid_50_50.png")).convert()
hard_grid_1_image = pygame.image.load(os.path.join(dir_path, "Sources", "1_grid_35_35.png")).convert()
hard_grid_2_image = pygame.image.load(os.path.join(dir_path, "Sources", "2_grid_35_35.png")).convert()
hard_grid_3_image = pygame.image.load(os.path.join(dir_path, "Sources", "3_grid_35_35.png")).convert()
hard_grid_4_image = pygame.image.load(os.path.join(dir_path, "Sources", "4_grid_35_35.png")).convert()
hard_grid_5_image = pygame.image.load(os.path.join(dir_path, "Sources", "5_grid_35_35.png")).convert()
hard_grid_6_image = pygame.image.load(os.path.join(dir_path, "Sources", "6_grid_35_35.png")).convert()
hard_grid_7_image = pygame.image.load(os.path.join(dir_path, "Sources", "7_grid_35_35.png")).convert()
hard_grid_8_image = pygame.image.load(os.path.join(dir_path, "Sources", "8_grid_35_35.png")).convert()
lose_image = pygame.image.load(os.path.join(dir_path, "Sources", "lose.png")).convert()
win_image = pygame.image.load(os.path.join(dir_path, "Sources", "win.png")).convert()
easy_flag_image = pygame.image.load(os.path.join(dir_path, "Sources", "flag_80_80.png")).convert()
medium_flag_image = pygame.image.load(os.path.join(dir_path, "Sources", "flag_50_50.png")).convert()
hard_flag_image = pygame.image.load(os.path.join(dir_path, "Sources", "flag_35_35.png")).convert()

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
    def __init__(self, image, pos, difficulty, status = 'none', opened = False, work = True, flagged = False):
        self.image = image
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.status = status
        self.difficulty = difficulty
        self.opened = opened
        self.work = work
        self.flagged = flagged
    
    def draw(self):
        screen.blit(self.image, self.rect)

    def disappear(self):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)
    
    def flag(self, image):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)
        screen.blit(image, self.rect)
        self.work = False
        self.flagged = True

    def unflag(self, image):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)
        screen.blit(image, self.rect)
        self.work = True
        self.flagged = False

    def change(self):
        pygame.draw.rect(screen, "#D3D3D3", self.rect)
        if self.difficulty == 'easy':
            if self.status == 'none':
                screen.blit(easy_grid_0_image, self.rect)
            elif self.status == 'mine':
                screen.blit(easy_grid_mine_image, self.rect)
            elif self.status == '1':
                screen.blit(easy_grid_1_image, self.rect)
            elif self.status == '2':
                screen.blit(easy_grid_2_image, self.rect)
            elif self.status == '3':
                screen.blit(easy_grid_3_image, self.rect)
            elif self.status == '4':
                screen.blit(easy_grid_4_image, self.rect)
            elif self.status == '5':
                screen.blit(easy_grid_5_image, self.rect)
            elif self.status == '6':
                screen.blit(easy_grid_6_image, self.rect)
            elif self.status == '7':
                screen.blit(easy_grid_7_image, self.rect)
            elif self.status == '8':
                screen.blit(easy_grid_8_image, self.rect)
        elif self.difficulty == 'medium':
            if self.status == 'none':
                screen.blit(medium_grid_0_image, self.rect)
            elif self.status == 'mine':
                screen.blit(medium_grid_mine_image, self.rect)
            elif self.status == '1':
                screen.blit(medium_grid_1_image, self.rect)
            elif self.status == '2':
                screen.blit(medium_grid_2_image, self.rect)
            elif self.status == '3':
                screen.blit(medium_grid_3_image, self.rect)
            elif self.status == '4':
                screen.blit(medium_grid_4_image, self.rect)
            elif self.status == '5':
                screen.blit(medium_grid_5_image, self.rect)
            elif self.status == '6':
                screen.blit(medium_grid_6_image, self.rect)
            elif self.status == '7':
                screen.blit(medium_grid_7_image, self.rect)
            elif self.status == '8':
                screen.blit(medium_grid_8_image, self.rect)
        elif self.difficulty == 'hard':
            if self.status == 'none':
                screen.blit(hard_grid_0_image, self.rect)
            elif self.status == 'mine':
                screen.blit(hard_grid_mine_image, self.rect)
            elif self.status == '1':
                screen.blit(hard_grid_1_image, self.rect)
            elif self.status == '2':
                screen.blit(hard_grid_2_image, self.rect)
            elif self.status == '3':
                screen.blit(hard_grid_3_image, self.rect)
            elif self.status == '4':
                screen.blit(hard_grid_4_image, self.rect)
            elif self.status == '5':
                screen.blit(hard_grid_5_image, self.rect)
            elif self.status == '6':
                screen.blit(hard_grid_6_image, self.rect)
            elif self.status == '7':
                screen.blit(hard_grid_7_image, self.rect)
            elif self.status == '8':
                screen.blit(hard_grid_8_image, self.rect)
        self.opened = True

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

lose = title(
    (600, 400),
    lose_image,
    10
)

win = title(
    (600, 400),
    win_image,
    10
)

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
            globals()[f"easy_grid_{i}"] = grid(easy_grid_image, (80 * (n + 2), 80 * (globals()[f"y{n}"])), 'easy')
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
            globals()[f"medium_grid_{i}"] = grid(medium_grid_image, (50 * (n + 2) + 25, 50 * (globals()[f"y{n}"] + 1)-50), 'medium')
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
            globals()[f"hard_grid_{i}"] = grid(hard_grid_image, (35 * (n + 2) + 57.5, 35 * (globals()[f"y{n}"] + 1)), 'hard')
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

        left_clicked = 0
        right_clicked = 1
        both_clicked = 1
        left_click = False
        right_click = False
        both_click = False
        click = 0
        game_over = False
        #game loop for game play
        easy_loop = True
        while easy_loop == True:
    
            if game_over != True:
                x,y = pygame.mouse.get_pos()
                #player left click
                if pygame.mouse.get_pressed()[0] == 1 and left_clicked == 1:
                    if 120 <= x <= 1080 and 40 <= y <= 760:
                        n = floor(x / 80 - 0.5) - 1 + floor(y / 80 - 0.5) * 12
                        click += 1
                    else:
                        n = -1
                    left_clicked += 1
                    left_click = True
                #player right click
                elif pygame.mouse.get_pressed()[2] == 1 and right_clicked == 1:
                    if 120 <= x <= 1080 and 40 <= y <= 760:
                        n = floor(x / 80 - 0.5) - 1 + floor(y / 80 - 0.5) * 12
                    else:
                        n = -1
                    right_clicked += 1
                    right_click = True
                #player click both at the same time
                elif pygame.mouse.get_pressed()[0] == 1 and pygame.mouse.get_pressed()[2] == 1 and both_clicked == 1:
                    if 120 <= x <= 1080 and 40 <= y <= 760:
                        n = floor(x / 80 - 0.5) - 1 + floor(y / 80 - 0.5) * 12
                    else:
                        n = -1
                    both_clicked += 1
                    both_click = True

                if pygame.mouse.get_pressed()[0] == 0:
                    left_clicked = 1
                if pygame.mouse.get_pressed()[2] == 0:
                    right_clicked = 1
                if pygame.mouse.get_pressed()[2] == 0 and pygame.mouse.get_pressed()[0] == 0:
                    both_clicked = 1
                
            #action 
            if 0 <= n <= 107:
                #detecting which status the clicked grid is and respond with various actions
                if left_click == True and click != 1:
                    if globals()[f'easy_grid_{n}'].work == True:
                        globals()[f'easy_grid_{n}'].change()
                    else:
                        pass

                #first click
                elif left_click == True and click == 1:
                    #random mines generation

                    number_list = list(range(0, 108))
                    remove_list = [n, n + 1, n - 1, n - 12, n - 13, n - 11, n + 12, n + 11, n + 13]
                    for number in remove_list:
                        for remove in number_list:
                            if number == remove:
                                number_list.remove(number)
                    randomlist = random.sample(number_list, 15)
                    for number in randomlist:
                        globals()[f'easy_grid_{number}'].status = 'mine'

                    #every grid status generation
                    for l in list(range(0, 108)):
                        counter = 0
                        if l % 12 == 0:
                            for i in [l + 1, l + 12, l + 13, l - 11, l - 12]:
                                if 0 <= i <= 107:
                                    if globals()[f'easy_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        elif l % 12 == 11:
                            for i in [l - 1, l + 11, l + 12, l - 12, l - 13]:
                                if 0 <= i <= 107:
                                    if globals()[f'easy_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        else:
                            for i in [l + 1, l - 1, l + 11, l + 12, l + 13, l - 11, l - 12, l - 13]:
                                if 0 <= i <= 107:
                                    if globals()[f'easy_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        if globals()[f'easy_grid_{l}'].status == 'mine':
                            globals()[f'easy_grid_{l}'].status = 'mine'
                        elif counter == 0:
                            globals()[f'easy_grid_{l}'].status = 'none'
                        elif counter == 1:
                            globals()[f'easy_grid_{l}'].status = '1'
                        elif counter == 2:
                            globals()[f'easy_grid_{l}'].status = '2'
                        elif counter == 3:
                            globals()[f'easy_grid_{l}'].status = '3'
                        elif counter == 4:
                            globals()[f'easy_grid_{l}'].status = '4'
                        elif counter == 5:
                            globals()[f'easy_grid_{l}'].status = '5'
                        elif counter == 6:
                            globals()[f'easy_grid_{l}'].status = '6'
                        elif counter == 7:
                            globals()[f'easy_grid_{l}'].status = '7'
                        elif counter == 8:
                            globals()[f'easy_grid_{l}'].status = '8'

                    globals()[f'easy_grid_{n}'].change()
                
                #right click flag
                elif right_click == True and globals()[f'easy_grid_{n}'].flagged == False and globals()[f'easy_grid_{n}'].opened == False:
                    globals()[f'easy_grid_{n}'].flag(easy_flag_image)
                
                #right click unflag
                elif right_click == True and globals()[f'easy_grid_{n}'].flagged == True and globals()[f'easy_grid_{n}'].opened == False:
                    globals()[f'easy_grid_{n}'].unflag(easy_grid_image)
                
                #convenient shortcut
                elif both_click == True and globals()[f'easy_grid_{n}'].opened == True:
                    counter = 0
                    if n % 12 == 0:
                            for i in [n + 1, n + 12, n + 13, n - 11, n - 12]:
                                if 0 <= i <= 107:
                                    if globals()[f'easy_grid_{i}'].flagged == True:
                                        counter += 1
                    elif n % 12 == 11:
                        for i in [n - 1, n + 11, n + 12, n - 12, n - 13]:
                            if 0 <= i <= 107:
                                if globals()[f'easy_grid_{i}'].flagged == True:
                                    counter += 1
                    else:
                        for i in [n + 1, n - 1, n + 11, n + 12, n + 13, n - 11, n - 12, n - 13]:
                            if 0 <= i <= 107:
                                if globals()[f'easy_grid_{i}'].flagged == True:
                                    counter += 1
                    if counter == 1:
                        counter = '1'
                    elif counter == 2:
                        counter = '2'
                    elif counter == 3:
                        counter = '3'
                    elif counter == 4:
                        counter = '4'
                    elif counter == 5:
                        counter = '5'
                    elif counter == 6:
                        counter = '6'
                    elif counter == 7:
                        counter = '7'
                    elif counter == 8:
                        counter = '8'
                    if globals()[f'easy_grid_{n}'].status == counter:
                        if n % 12 == 0:
                            for i in [n + 1, n + 12, n + 13, n - 11, n - 12]:
                                if 0 <= i <= 107:
                                    if globals()[f'easy_grid_{i}'].flagged != True:
                                        globals()[f'easy_grid_{i}'].change()
                        elif n % 12 == 11:
                            for i in [n - 1, n + 11, n + 12, n - 12, n - 13]:
                                if 0 <= i <= 107:
                                    if globals()[f'easy_grid_{i}'].flagged != True:
                                        globals()[f'easy_grid_{i}'].change()
                        else:
                            for i in [n + 1, n - 1, n + 11, n + 12, n + 13, n - 11, n - 12, n - 13]:
                                if 0 <= i <= 107:
                                    if globals()[f'easy_grid_{i}'].flagged != True:
                                        globals()[f'easy_grid_{i}'].change()

            else:
                pass
            
            #losing detection
            game_lose = False
            if game_over != True:
                for i in range(0, 108):
                    if globals()[f'easy_grid_{i}'].status == 'mine' and globals()[f'easy_grid_{i}'].opened == True and game_over != True:
                        game_over = True
                        game_lose = True
            if game_over == True and game_lose == True:
                for i in range(0, 108):
                    globals()[f'easy_grid_{i}'].change()
                lose.show()
                game_over = True

            #winning detection
            if game_over != True:
                counter = 0
                for i in range(0, 108):
                    if globals()[f'easy_grid_{i}'].opened == True:
                        counter += 1
                    elif globals()[f'easy_grid_{i}'].flagged == True and globals()[f'easy_grid_{i}'].status == 'mine':
                        counter += 1
                if counter == 108:
                    win.show()
                    game_over = True

            #open all the 0 squares
                
            if game_over != True:
                for n in range(0, 108):
                    if globals()[f'easy_grid_{n}'].status == 'none' and globals()[f'easy_grid_{n}'].opened == True:
                        if n % 12 == 0:
                            for i in [n + 1, n + 12, n + 13, n - 11, n - 12]:
                                if 0 <= i <= 107:
                                    globals()[f'easy_grid_{i}'].change()
                        elif n % 12 == 11:
                            for i in [n - 1, n + 11, n + 12, n - 12, n - 13]:
                                if 0 <= i <= 107:
                                    globals()[f'easy_grid_{i}'].change()
                        else:
                            for i in [n + 1, n - 1, n + 11, n + 12, n + 13, n - 11, n - 12, n - 13]:
                                if 0 <= i <= 107:
                                    globals()[f'easy_grid_{i}'].change()
                        
            left_click = False
            right_click = False
            both_click = False

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

        #wipe all the previous game data
        i = 0
        while i < 108:
            globals()[f"easy_grid_{i}"].status = 'none'
            globals()[f"easy_grid_{i}"].opened = False
            globals()[f"easy_grid_{i}"].flagged = False
            globals()[f"easy_grid_{i}"].work = True
            i += 1

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

        left_clicked = 0
        right_clicked = 1
        both_clicked = 1
        left_click = False
        right_click = False
        both_click = False
        click = 0
        game_over = False
        #game loop for game play
        medium_loop = True
        while medium_loop == True:

            if game_over != True:

                x,y = pygame.mouse.get_pos()
                #player left click
                if pygame.mouse.get_pressed()[0] == 1 and left_clicked == 1:
                    if 100 <= x <= 1100 and 25 <= y <= 775:
                        n = floor(x / 50) - 2 + floor(y / 50 - 0.5) * 20
                        click += 1
                    else:
                        n = -1
                    left_clicked += 1
                    left_click = True
                #player right click
                elif pygame.mouse.get_pressed()[2] == 1 and right_clicked == 1:
                    if 100 <= x <= 1100 and 25 <= y <= 775:
                        n = floor(x / 50) - 2 + floor(y / 50 - 0.5) * 20
                    else:
                        n = -1
                    right_clicked += 1
                    right_click = True
                #player click both at the same time
                elif pygame.mouse.get_pressed()[0] == 1 and pygame.mouse.get_pressed()[2] == 1 and both_clicked == 1:
                    if 100 <= x <= 1100 and 25 <= y <= 775:
                        n = floor(x / 50) - 2 + floor(y / 50 - 0.5) * 20
                    else:
                        n = -1
                    both_clicked += 1
                    both_click = True

                if pygame.mouse.get_pressed()[0] == 0:
                    left_clicked = 1
                if pygame.mouse.get_pressed()[2] == 0:
                    right_clicked = 1
                if pygame.mouse.get_pressed()[2] == 0 and pygame.mouse.get_pressed()[0] == 0:
                    both_clicked = 1

            #action 
            if 0 <= n <= 299:
                #detecting which status the clicked grid is and respond with various actions
                if left_click == True and click != 1:
                    if globals()[f'medium_grid_{n}'].work == True:
                        globals()[f'medium_grid_{n}'].change()
                        

                #first click
                elif left_click == True and click == 1:
                    #random mines generation
                    number_list = list(range(0, 300))
                    remove_list = [n, n + 1, n - 1, n - 21, n - 20, n - 19, n + 20, n + 19, n + 21]
                    for number in remove_list:
                        for numbers in number_list:
                            if number == numbers:
                                number_list.remove(number)
                    randomlist = random.sample(number_list, 50)
                    for number in randomlist:
                        globals()[f'medium_grid_{number}'].status = 'mine'

                    #every grid status generation
                    for l in list(range(0, 300)):
                        counter = 0
                        if l % 20 == 0:
                            for i in [l + 1, l + 20, l + 21, l - 19, l - 20]:
                                if 0 <= i <= 299:
                                    if globals()[f'medium_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        elif l % 20 == 19:
                            for i in [l - 1, l + 20, l + 19, l - 20, l - 21]:
                                if 0 <= i <= 299:
                                    if globals()[f'medium_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        else:
                            for i in [l + 1, l - 1, l + 20, l + 21, l + 19, l - 20, l - 19, l - 21]:
                                if 0 <= i <= 299:
                                    if globals()[f'medium_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        if globals()[f'medium_grid_{l}'].status == 'mine':
                            globals()[f'medium_grid_{l}'].status = 'mine'
                        elif counter == 0:
                            globals()[f'medium_grid_{l}'].status = 'none'
                        elif counter == 1:
                            globals()[f'medium_grid_{l}'].status = '1'
                        elif counter == 2:
                            globals()[f'medium_grid_{l}'].status = '2'
                        elif counter == 3:
                            globals()[f'medium_grid_{l}'].status = '3'
                        elif counter == 4:
                            globals()[f'medium_grid_{l}'].status = '4'
                        elif counter == 5:
                            globals()[f'medium_grid_{l}'].status = '5'
                        elif counter == 6:
                            globals()[f'medium_grid_{l}'].status = '6'
                        elif counter == 7:
                            globals()[f'medium_grid_{l}'].status = '7'
                        elif counter == 8:
                            globals()[f'medium_grid_{l}'].status = '8'

                    globals()[f'medium_grid_{n}'].change()

                #right click flag
                elif right_click == True and globals()[f'medium_grid_{n}'].flagged == False and globals()[f'medium_grid_{n}'].opened == False:
                    globals()[f'medium_grid_{n}'].flag(medium_flag_image)
                
                #right click unflag
                elif right_click == True and globals()[f'medium_grid_{n}'].flagged == True and globals()[f'medium_grid_{n}'].opened == False:
                    globals()[f'medium_grid_{n}'].unflag(medium_grid_image)
                
                #convenient shortcut
                elif both_click == True and globals()[f'medium_grid_{n}'].opened == True:
                    counter = 0
                    if n % 20 == 0:
                        for i in [n + 1, n + 20, n + 21, n - 19, n - 20]:
                            if 0 <= i <= 299:
                                if globals()[f'medium_grid_{i}'].flagged == True:
                                    counter += 1
                    elif n % 20 == 19:
                        for i in [n - 1, n + 19, n + 20, n - 21, n - 20]:
                            if 0 <= i <= 299:
                                if globals()[f'medium_grid_{i}'].flagged == True:
                                    counter += 1
                    else:
                        for i in [n + 1, n - 1, n + 20, n + 21, n + 19, n - 19, n - 21, n - 20]:
                            if 0 <= i <= 299:
                                if globals()[f'medium_grid_{i}'].flagged == True:
                                    counter += 1
                    if counter == 1:
                        counter = '1'
                    elif counter == 2:
                        counter = '2'
                    elif counter == 3:
                        counter = '3'
                    elif counter == 4:
                        counter = '4'
                    elif counter == 5:
                        counter = '5'
                    elif counter == 6:
                        counter = '6'
                    elif counter == 7:
                        counter = '7'
                    elif counter == 8:
                        counter = '8'
                    if globals()[f'medium_grid_{n}'].status == counter:
                        if n % 20 == 0:
                            for i in [n + 1, n + 20, n + 21, n - 19, n - 20]:
                                if 0 <= i <= 299:
                                    if globals()[f'medium_grid_{i}'].flagged != True:
                                        globals()[f'medium_grid_{i}'].change()
                        elif n % 20 == 19:
                            for i in [n - 1, n + 19, n + 20, n - 21, n - 20]:
                                if 0 <= i <= 299:
                                    if globals()[f'medium_grid_{i}'].flagged != True:
                                        globals()[f'medium_grid_{i}'].change()
                        else:
                            for i in [n + 1, n - 1, n + 20, n + 21, n + 19, n - 19, n - 21, n - 20]:
                                if 0 <= i <= 299:
                                    if globals()[f'medium_grid_{i}'].flagged != True:
                                        globals()[f'medium_grid_{i}'].change()

            else:
                pass
            
            #losing detection
            game_lose = False
            if game_over != True:
                for i in range(0, 300):
                    if globals()[f'medium_grid_{i}'].status == 'mine' and globals()[f'medium_grid_{i}'].opened == True and game_over != True:
                        game_over = True
                        game_lose = True
            if game_over == True and game_lose == True:
                for i in range(0, 300):
                    globals()[f'medium_grid_{i}'].change()
                lose.show()
                game_over = True

            #winning detection
            if game_over != True:
                counter = 0
                for i in range(0, 300):
                    if globals()[f'medium_grid_{i}'].opened == True:
                        counter += 1
                    elif globals()[f'medium_grid_{i}'].flagged == True and globals()[f'medium_grid_{i}'].status == 'mine':
                        counter += 1
                if counter == 300:
                    win.show()
                    game_over = True
        
            #open all the 0 squares
                
            if game_over != True:
                for n in range(0, 300):
                    if globals()[f'medium_grid_{n}'].status == 'none' and globals()[f'medium_grid_{n}'].opened == True:
                        if n % 20 == 0:
                            for i in [n + 1, n + 20, n + 21, n - 19, n - 20]:
                                if 0 <= i <= 299:
                                    globals()[f'medium_grid_{i}'].change()
                        elif n % 20 == 19:
                            for i in [n - 1, n + 19, n + 20, n - 21, n - 20]:
                                if 0 <= i <= 299:
                                    globals()[f'medium_grid_{i}'].change()
                        else:
                            for i in [n + 1, n - 1, n + 20, n + 21, n + 19, n - 19, n - 21, n - 20]:
                                if 0 <= i <= 299:
                                    globals()[f'medium_grid_{i}'].change()
            left_click = False
            right_click = False
            both_click = False

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

        #wipe all the previous game data
        i = 0
        while i < 300:
            globals()[f"medium_grid_{i}"].status = 'none'
            globals()[f"medium_grid_{i}"].opened = False
            globals()[f"medium_grid_{i}"].flagged = False
            globals()[f"medium_grid_{i}"].work = True
            i += 1

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

        left_clicked = 0
        right_clicked = 1
        both_clicked = 1
        left_click = False
        right_click = False
        both_click = False
        click = 0
        game_over = False
        #game loop for game play
        hard_loop = True
        while hard_loop == True:
            
            if game_over != True:

                x,y = pygame.mouse.get_pos()
                #player left click
                if pygame.mouse.get_pressed()[0] == 1 and left_clicked == 1:
                    if 110 <= x <= 1090 and 52.5 <= y <= 787.5:
                        n = floor(x / 35 - 1/7) - 3 + (floor(y / 35 - 0.5) - 1) * 28
                        click += 1
                    else:
                        n = -1
                    left_clicked += 1
                    left_click = True
                #player right click
                elif pygame.mouse.get_pressed()[2] == 1 and right_clicked == 1:
                    if 110 <= x <= 1090 and 52.5 <= y <= 787.5:
                        n = floor(x / 35 - 1/7) - 3 + (floor(y / 35 - 0.5) - 1) * 28
                    else:
                        n = -1
                    right_clicked += 1
                    right_click = True
                #player click both at the same time
                elif pygame.mouse.get_pressed()[0] == 1 and pygame.mouse.get_pressed()[2] == 1 and both_clicked == 1:
                    if 110 <= x <= 1090 and 52.5 <= y <= 787.5:
                        n = floor(x / 35 - 1/7) - 3 + (floor(y / 35 - 0.5) - 1) * 28
                    else:
                        n = -1
                    both_clicked += 1
                    both_click = True

                if pygame.mouse.get_pressed()[0] == 0:
                    left_clicked = 1
                if pygame.mouse.get_pressed()[2] == 0:
                    right_clicked = 1
                if pygame.mouse.get_pressed()[2] == 0 and pygame.mouse.get_pressed()[0] == 0:
                    both_clicked = 1

            #action 
            if 0 <= n <= 587:
                #detecting which status the clicked grid is and respond with various actions
                if left_click == True and click != 1:
                    if globals()[f'hard_grid_{n}'].work == True:
                        globals()[f'hard_grid_{n}'].change()

                #first click
                elif left_click == True and click == 1:
                    #random mines generation
                    number_list = list(range(0, 588))
                    remove_list = [n, n + 1, n - 1, n - 28, n - 29, n - 27, n + 28, n + 29, n + 27]
                    for number in remove_list:
                        for remove in number_list:
                            if number == remove:
                                number_list.remove(number)
                    randomlist = random.sample(number_list, 150)
                    for number in randomlist:
                        globals()[f'hard_grid_{number}'].status = 'mine'

                    #every grid status generation
                    for l in list(range(0, 588)):
                        counter = 0
                        if l % 28 == 0:
                            for i in [l + 1, l + 28, l + 29, l - 27, l - 28]:
                                if 0 <= i <= 587:
                                    if globals()[f'hard_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        elif l % 28 == 27:
                            for i in [l - 1, l + 28, l + 27, l - 28, l - 29]:
                                if 0 <= i <= 587:
                                    if globals()[f'hard_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        else:
                            for i in [l + 1, l - 1, l + 28, l + 29, l + 27, l - 28, l - 29, l - 27]:
                                if 0 <= i <= 587:
                                    if globals()[f'hard_grid_{i}'].status == 'mine':
                                        counter += 1
                                else:
                                    pass
                        if globals()[f'hard_grid_{l}'].status == 'mine':
                            globals()[f'hard_grid_{l}'].status = 'mine'
                        elif counter == 0:
                            globals()[f'hard_grid_{l}'].status = 'none'
                        elif counter == 1:
                            globals()[f'hard_grid_{l}'].status = '1'
                        elif counter == 2:
                            globals()[f'hard_grid_{l}'].status = '2'
                        elif counter == 3:
                            globals()[f'hard_grid_{l}'].status = '3'
                        elif counter == 4:
                            globals()[f'hard_grid_{l}'].status = '4'
                        elif counter == 5:
                            globals()[f'hard_grid_{l}'].status = '5'
                        elif counter == 6:
                            globals()[f'hard_grid_{l}'].status = '6'
                        elif counter == 7:
                            globals()[f'hard_grid_{l}'].status = '7'
                        elif counter == 8:
                            globals()[f'hard_grid_{l}'].status = '8'

                    globals()[f'hard_grid_{n}'].change()

                #right click flag
                elif right_click == True and globals()[f'hard_grid_{n}'].flagged == False and globals()[f'hard_grid_{n}'].opened == False:
                    globals()[f'hard_grid_{n}'].flag(hard_flag_image)
                
                #right click unflag
                elif right_click == True and globals()[f'hard_grid_{n}'].flagged == True and globals()[f'hard_grid_{n}'].opened == False:
                    globals()[f'hard_grid_{n}'].unflag(hard_grid_image)
                
                #convenient shortcut
                elif both_click == True and globals()[f'hard_grid_{n}'].opened == True:
                    counter = 0
                    if n % 28 == 0:
                        for i in [n + 1, n + 28, n + 29, n - 27, n - 28]:
                            if 0 <= i <= 587:
                                if globals()[f'hard_grid_{i}'].flagged == True:
                                    counter += 1
                    elif n % 28 == 27:
                        for i in [n - 1, n + 27, n + 28, n - 29, n - 28]:
                            if 0 <= i <= 587:
                                if globals()[f'hard_grid_{i}'].flagged == True:
                                    counter += 1
                    else:
                        for i in [n + 1, n - 1, n + 27, n + 28, n + 29, n - 27, n - 28, n - 29]:
                            if 0 <= i <= 587:
                                if globals()[f'hard_grid_{i}'].flagged == True:
                                    counter += 1
                    if counter == 1:
                        counter = '1'
                    elif counter == 2:
                        counter = '2'
                    elif counter == 3:
                        counter = '3'
                    elif counter == 4:
                        counter = '4'
                    elif counter == 5:
                        counter = '5'
                    elif counter == 6:
                        counter = '6'
                    elif counter == 7:
                        counter = '7'
                    elif counter == 8:
                        counter = '8'
                    if globals()[f'hard_grid_{n}'].status == counter:
                        if n % 28 == 0:
                            for i in [n + 1, n + 28, n + 29, n - 27, n - 28]:
                                if 0 <= i <= 587:
                                    if globals()[f'hard_grid_{i}'].flagged != True:
                                        globals()[f'hard_grid_{i}'].change()
                        elif n % 28 == 27:
                            for i in [n - 1, n + 27, n + 28, n - 29, n - 28]:
                                if 0 <= i <= 587:
                                    if globals()[f'hard_grid_{i}'].flagged != True:
                                        globals()[f'hard_grid_{i}'].change()
                        else:
                            for i in [n + 1, n - 1, n + 27, n + 28, n + 29, n - 27, n - 28, n - 29]:
                                if 0 <= i <= 587:
                                    if globals()[f'hard_grid_{i}'].flagged != True:
                                        globals()[f'hard_grid_{i}'].change()

            else:
                pass
            
            #losing detection
            game_lose = False
            if game_over != True:
                for i in range(0, 588):
                    if globals()[f'hard_grid_{i}'].status == 'mine' and globals()[f'hard_grid_{i}'].opened == True and game_over != True:
                        game_over = True
                        game_lose = True
            if game_over == True and game_lose == True:
                for i in range(0, 588):
                    globals()[f'hard_grid_{i}'].change()
                lose.show()
                game_over = True

            #winning detection
            if game_over != True:
                counter = 0
                for i in range(0, 588):
                    if globals()[f'hard_grid_{i}'].opened == True:
                        counter += 1
                    elif globals()[f'hard_grid_{i}'].flagged == True and globals()[f'hard_grid_{i}'].status == 'mine':
                        counter += 1
                if counter == 588:
                    win.show()
                    game_over = True
            
            #open all the 0 squares
                
            if game_over != True:
                for n in range(0, 588):
                    if globals()[f'hard_grid_{n}'].status == 'none' and globals()[f'hard_grid_{n}'].opened == True:
                        if n % 28 == 0:
                            for i in [n + 1, n + 28, n + 29, n - 27, n - 28]:
                                if 0 <= i <= 587:
                                    globals()[f'hard_grid_{i}'].change()
                        elif n % 28 == 27:
                            for i in [n - 1, n + 27, n + 28, n - 29, n - 28]:
                                if 0 <= i <= 587:
                                    globals()[f'hard_grid_{i}'].change()
                        else:
                            for i in [n + 1, n - 1, n + 28, n + 29, n + 27, n - 27, n - 28, n - 29]:
                                if 0 <= i <= 587:
                                    globals()[f'hard_grid_{i}'].change()
            left_click = False
            right_click = False
            both_click = False

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

        #wipe all the previous game data
        i = 0
        while i < 588:
            globals()[f"hard_grid_{i}"].status = 'none'
            globals()[f"hard_grid_{i}"].opened = False
            globals()[f"hard_grid_{i}"].flagged = False
            globals()[f"hard_grid_{i}"].work = True
            i += 1

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
        