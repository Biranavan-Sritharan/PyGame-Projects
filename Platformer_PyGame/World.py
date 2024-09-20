import pygame
from Enemy import Enemy #for the Enemy() functionality
from Flag import Flag

class World():
      def __init__(self, world_data,tile_size, walrus_group, flag_group):
            self.tile_list = []
            block = pygame.image.load('assets/Block.png')
            grass = pygame.image.load('assets/Grass.png')
            flag = pygame.image.load('assets/Flag.png')

            row_count = 0
            for row in world_data: #so the [1,1,1,1,1] -> is a row of the 4 other rows, so row selected, in this case row 0
                  col_count = 0
                  for tile in row: #then each column (each element) has a tile value, so 1 being dirt, 2 being grass etc. #so for each element in the array it iterates thru
                        if tile == 1:
                              img = pygame.transform.scale(block , (tile_size, tile_size)) #we got tile loaded up BUT need coords to place
                              img_rect = img.get_rect() #so here inbuilt PyGame function, it takes current tile image size and makes a rectangle from it (no draw rect or anything like that)
                              img_rect.x = col_count * tile_size #x coord, needs to be defined to where it is in the list, so tile size = 100, then x coord need to increase from 0,100,200,300,400,500. To fill in each grid box properly
                              img_rect.y = row_count * tile_size #y coord, so row_count * tile_size works by e.g. row_count = 2, tile_size = 100. 2 * 100 = 200. So the tile will have a y coordinate of 200
                              tile = (img, img_rect) #now the newley defined values in the variables are put into a tuple and saved in the tile variable
                              self.tile_list.append(tile) #the tile var is added to the new list, the world_data array is used just once to initally load in the world. Data saved in this new array tile_list
                        if tile == 2:
                              img = pygame.transform.scale(grass , (tile_size, tile_size))
                              img_rect = img.get_rect()
                              img_rect.x = col_count * tile_size
                              img_rect.y = row_count * tile_size
                              tile = (img, img_rect)
                              self.tile_list.append(tile)
                        if tile == 3:
                               walrus = Enemy(col_count * tile_size, row_count * tile_size + 30) #determine the positoning of the enemy on the grid
                               walrus_group.add(walrus)  #like an array, it append the walrus to the group to then be displayed if walrus_group.draw() is called
                        if tile == 4:
                               flag = Flag(col_count * tile_size, row_count * tile_size +20)
                               flag_group.add(flag)
                        col_count += 1
                  row_count += 1

      def draw(self,screen): #need to draw tiles to screen
        for tile in self.tile_list: #so in the new list, goes thru each element
                        screen.blit(tile[0], tile[1]) #so tile[0] is the tile img and tile[1] is the rect (so the rect coorsd)
                        #pygame.draw.rect(screen, (255,255,255), tile[1], 2) #show tile hitboxes
