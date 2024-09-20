import pygame

class Player():
    def __init__(self,x,y,world):
        self.world = world #don't need to import World here jsut this is enough
        #self.game_over = game_over

        #animation
        self.animation_right = []
        self.animation_left = []
        self.index = 0
        self.counter = 0
        self.direction = 1

        for num in range (1,4):
            img_right = pygame.image.load(f'assets/CharAni{num}.png')
            img_right = pygame.transform.scale(img_right, (70,80))
            img_left = pygame.transform.flip(img_right, True, False) #true and false is flipping on the x and y axis respectively, so y is false otherwise image would be upside down
            self.animation_right.append(img_right)
            self.animation_left.append(img_left)
        self.image = self.animation_right[self.index] 
        

        character = pygame.image.load('assets/CharAni1.png')  #loads char image and adds to character var
        self.image = pygame.transform.scale(character, (70,80)) #transform char size and adds it to var self.image
        self.rect = self.image.get_rect() #overlaying a rectangle over player char to get x and y coords ##BASICALLY HITBOX
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0 #used for jump and gravity
        self.jump = False

    def update(self, screen, walrus_group, game_over, refresh, flag_group, level_num): #walrus_group passed in for enemy collision check!
        #delta change
        dx = 0
        dy = 0
        anim_cooldown = 20

        if game_over == 0:
            #player controls
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                #self.rect.x -= 2 #now dx affects player movement since this was affecting the collision, since when there was an x collsion is affected the original self.rect.x value (too early??)
                dx -= 2
                self.counter += 1 #animation
                self.direction = 0 #animation direction
            if key[pygame.K_d]:
                #self.rect.x += 2
                dx += 2
                self.counter += 1 #aniamtion
                self.direction = 1 #animation direction
            #idle animation
            if key[pygame.K_d] == False and key[pygame.K_a] == False: 
                if self.direction == 1:
                    self.image = self.animation_right[0]
                elif self.direction == 0:
                    self.image = self.animation_left[0]
            #JUMP
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -5
                self.jump = True
            #if key[pygame.K_w] == False: #this checks if the W is NO LONGER pressed down, therefore changing self.jump to false otherwise self.jump will be permanetly be set to true and therfore can not jump again
                #self.jump = False
                #pass

            #animation
            if self.direction == 1: #right side anim
                if self.counter > anim_cooldown:
                    self.counter = 0
                    self.index += 1
                    #print(len(self.animation_right))
                    if self.index >= len(self.animation_right):
                        self.index = 1
                    self.image = self.animation_right[self.index]
            elif self.direction == 0: #left side anim
                if self.counter > anim_cooldown:
                    self.counter = 0
                    self.index += 1
                    #print(len(self.animation_right))
                    if self.index >= len(self.animation_left):
                        self.index = 1
                    self.image = self.animation_left[self.index]

            #gravity
            self.vel_y += 0.1 #brings player downwards
            if self.vel_y > 10: #limit set (or a terminal velocity a player can reach)
                self.vel_y = 10
            dy += self.vel_y #this is how self.vel if affecting the rect coords (hence player coords), since dy affects player coords/rect coords

            ''' #old code to keep player on screen before collisions was added, now has no purpose
            #remove later
            if self.rect.bottom >= 500 and key[pygame.K_w] == False: #adding this extra 'and' allowed teh player to be FINALLY able to jump, keep in mind for collisons later on
                self.rect.bottom = 500                               
                dy = 0
            '''

            #collison check
            for tile in self.world.tile_list: #so tile_list is in another class, so saying CLASSNAME.tile_list can get it
                #x coord collision, so dx is basically movement value and self.rect.x is current value SO dx + current position would be the future position!
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.image.get_width(), self.image.get_height()):  #here the future x coords and current y coords of the player rect checks to see if it collides the tiles, also the image width and height are taken to make sure collision occurs with whole width and height
                    dx = 0 #stops player from moving in the x direction
                #y coords collision, because we can have collison in y but we dont want it to affect x since he should be able to move around soemtimes so x and y collisions is seperate
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                    #check if head hits block above
                    if self.vel_y < 0:  #so vel is -ve, so player is jumping
                        dy = tile[1].bottom - self.rect.top #so here it checks to see if the FUTURE palyer collides with hitbox, so it does it before colliding rather than when it has already intersected by seeing the diffrence it can move into and allows player to go into that space
                        self.vel_y = 0 #since vel_y is quite far into the negatives, it takes a while for it to reach a +ve to start falling, so without this the palyer would wait a bit before falling in the jumping motion
                    elif self.vel_y >= 0: #so vel is +ve, hence player falling
                        dy = tile[1].top - self.rect.bottom
                        self.jump = False #so this is here when it touches the GROUND, not in x collsion block since thats with the side of the tile/block not the top of the tile which is the ground!!!
            
            #Enemy collision
            if pygame.sprite.spritecollide(self, walrus_group, False): #False stops the walrus disappearing after collsion occurs
                game_over = 1
                #return game_over
            #print(game_over) #this prints out 1's when player collides with walrus, not reaching globally, so pass game_over thru update emthod??

            if pygame.sprite.spritecollide(self, flag_group, False): #collison with flag
                game_over = 2 #2 means win
                #level_num #this does nothing
                self.world.tile_list.clear() #removes the old level

                #print(level_num) #outputting 2 as it should

            #update player coords
            self.rect.x += dx  #dx and dy now directly cahnge the x and y coords of rect
            self.rect.y += dy

            #draw player
            #pygame.draw.rect(screen, (255,255,255) , self.rect ,2) #show hitbox ,the 4th param changes rect line thickness
            screen.blit(self.image, self.rect) #draws/updates player to screen

        elif game_over == 1:
            ghost = pygame.image.load('assets/Ghost.png')
            self.ghost = pygame.transform.scale(ghost, (35,35))
            self.rect_ghost = self.ghost.get_rect()
            self.rect_ghost.x = self.rect.x + (15)
            self.rect_ghost.y = self.rect.y
            screen.blit(self.ghost, self.rect_ghost)
            self.rect.y -= 5
            if self.rect.y < -25:
                self.rect.y = -50

        if refresh == 1:
            self.rect.x = 200
            self.rect.y = 370

        return game_over, level_num
    
    #def level_update(flag_group, level_num):
        