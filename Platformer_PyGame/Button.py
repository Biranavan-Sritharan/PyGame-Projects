import pygame

class Button():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        pygame.font.init()

        #restart button
        self.restart = pygame.font.SysFont('comicsans' , 30)
        self.button = self.restart.render("Restart" ,1 ,(255,0,255))
        self.rect = self.button.get_rect()
        self.rect.x = (self.screen_width // 2) - 45    
        self.rect.y = (self.screen_height // 2) - 30

        #start button
        self.start = pygame.font.SysFont('comicsans' , 50)
        self.start = self.start.render("Start" ,1 ,(255,0,255))
        self.start_rect = self.start.get_rect()
        self.start_rect.x = 190  
        self.start_rect.y = 85

        #NOT a button, Game Title for start menu
        self.game_title = pygame.font.SysFont('comicsans' , 65)
        self.game_title = self.game_title.render("OOP Platformer" ,1 ,(255,0,255))
        self.game_title_rect = self.game_title.get_rect()
        self.game_title_rect.x = 5  
        self.game_title_rect.y = 5

        #You Won Text
        self.win = pygame.font.SysFont('comicsans' , 70)
        self.win = self.win.render("You Won!" ,1 ,(255,0,255))
        self.rect_win = self.win.get_rect()
        self.rect_win.x = (self.screen_width // 2) -150 
        self.rect_win.y = (self.screen_height // 2) -100

        #Play again
        self.again = pygame.font.SysFont('comicsans' , 40)
        self.again = self.again.render("Play Again?" ,1 ,(255,0,255))
        self.rect_again = self.again.get_rect()
        self.rect_again.x = (self.screen_width // 2) -100   
        self.rect_again.y = (self.screen_height // 2) -20


    def update(self,screen, refresh):
        pos = pygame.mouse.get_pos()
        #print(pos)
        #pygame.draw.rect(screen , (255,255,0), self.rect, 2) #restart text button hitbox
        screen.blit(self.button , self.rect)

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:    #the get_pressed()[0], the [0] means LEFT mouse button, (1 is middle adn 2 is right?)
            refresh = 1
            return refresh
        
        #if game_over == 1 and mouse_pos == self.rect and mousebutton down
        #then self reshresh or wahtevs returns 1

    def start_update(self, screen, begin): #start menu function
        pos = pygame.mouse.get_pos()
        if begin == 0:
            screen.blit(self.start , self.start_rect)
            screen.blit(self.game_title, self.game_title_rect)

        if self.start_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            begin_condition = 1
            return begin_condition
        
    def game_won(self, screen, try_again):
        pos = pygame.mouse.get_pos()

        screen.blit(self.win, self.rect_win)
        screen.blit(self.again, self.rect_again)

        if self.rect_again.collidepoint(pos) and pygame.mouse.get_pressed()[0] == True:
            try_again = 1
            return try_again
        
        

        