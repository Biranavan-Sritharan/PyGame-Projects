import pygame

class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        flag = pygame.image.load('assets/Flag.png')
        self.image = pygame.transform.scale(flag, (70,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
