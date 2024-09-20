import pygame

class Enemy(pygame.sprite.Sprite): #so the enemy class is a child class of the inbuilt pygame class sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) #calling constrcutor from the super class of sprite
        walrus = pygame.image.load('assets/Walrus.png')
        self.image = pygame.transform.scale(walrus, (70,80))
        self.rect = self.image.get_rect()
        self.rect.x = x #pos walrus with passed in values
        self.rect.y = y #"
        self.move = 1 #used in walrus movement
        self.movement_counter = 1 #used for changing walrus direction

    def update(self,screen):
        self.rect.x += self.move
        self.movement_counter += 1
        if self.movement_counter == 45:
            self.move = -1 * (self.move)
            self.movement_counter = 0 #i dont want it to go past spawn block in my base :)
            #self.movement_counter *= -1 #flips the counter so that walrus goes past the spawnpoint rather than changing directions at spawnpoint
                                         # sometimes the abs() is used in the if statement if there is a -ve num problem

        #pygame.draw.rect(screen, (255,255,255), self.rect,2) #walrus hitbox


