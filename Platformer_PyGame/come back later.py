import pygame
import sys

tile_size = 200

world = [
    [1 , 1 , 1 , 1 , 1],
    [1 , 0 , 0 , 0 , 1],
    [1 , 0 , 0 , 0 , 1],
    [1 , 0 , 0 , 0 , 1],
    [1 , 0 , 0 , 0 , 1],
    [1 , 1 , 1 , 1 , 1],
]




class Game:
    #Constructor
    def __init__(self,data):
        pygame.init()

        #game window
        pygame.display.set_caption("OOP Platformer")
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width,self.height))

        #clock speed
        self.clock = pygame.time.Clock()

        #load Character to window
        self.image = pygame.image.load('assets/Character.png')
        self.image_pos = [160,260]
        self.movement = [False,False]

        self.tile_list = []

        ground_block = pygame.image.load('assets/Block.png')

        row_count = 0
        for row in data:
            col_count = 0

            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(ground_block, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (ground_block, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1


    #Game loop
    def run(self):
        while True:
            self.image_pos[1] += (self.movement[1] - self.movement[0]) *5
            self.screen.fill((14,219,248))
            self.screen.blit(self.image, self.image_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False
                    
            pygame.display.update()
            self.clock.tick(60)


world_ = Game(world)

Game().run()