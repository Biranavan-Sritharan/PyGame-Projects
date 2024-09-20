import pygame
from World import World
from Player import Player
#from Enemy import Enemy
from Button import Button

pygame.init()

#fps initial
clock = pygame.time.Clock()
fps = 60

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OOP Platformer")

#variables defined globally
tile_size = screen_width/5
game_over = 0
refresh = 0
begin = 0
level_num = 1
end_game = 0
try_again = 0

#draw grid
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

#removes walrus and flag from screen for level reset
def reset_level(level_num, end_game):
     level_num += 1
     end_game = 0

     if level_num > 2: #number of levels in game is 2, so cant go past that
          level_num -= 1
          end_game = 1

     walrus_group.empty()
     flag_group.empty()
     world_data = []
     #game_over = 0
     #begin = 1
    
     count = 0
     with open (f'levels/level{level_num}.txt' , 'r') as file:
        for x in file:
            a = [item.strip(',') for item in x.split()] #list comprehension, python data structures, look into later ##strip removes the , and split creates a new array at whitespace, so in this case the end of each line in the notepad file
            world_data.append(a)

        for x in world_data: #converting each value in array from string to int
            for y in x:
                y = int(y)
                x[count] = y
                count += 1
                if count >= len(x):
                    count = 0

     world = World(world_data, tile_size, walrus_group, flag_group)
     player.world = world #Telling player class about the new updated world, basically passing in that data, since world is taken into the player class

     return world, level_num, end_game

#world generation
def world_gen(level_num):
    world_data = []
    count = 0
    with open (f'levels/level{level_num}.txt' , 'r') as file:
        for x in file:
            a = [item.strip(',') for item in x.split()] #list comprehension, python data structures, look into later ##strip removes the , and split creates a new array at whitespace, so in this case the end of each line in the notepad file
            world_data.append(a)

        for x in world_data:
            for y in x:
                y = int(y)
                x[count] = y
                count += 1
                if count >= len(x):
                    count = 0
    return world_data

world_data = world_gen(level_num) #calling world gen function and then making world_data var global in main.py

#OBJECTS
walrus_group = pygame.sprite.Group() #enemy class, also above world object since this needs to be passed into the world constructor
flag_group = pygame.sprite.Group()
#world and player objects which are calling the constructors of their respective class
world = World(world_data, tile_size, walrus_group, flag_group) #tile_size needs to be passed to World class too ##Now this is also passing in the Enemy class (walrus_group so it can be loaded onto a tile) 
#print(world.tile_list) #u can see tuple of tile img and img_rect
player = Player(200, screen_height - 180, world) #passing the player class into a var, with x and y pos of player ##now also added the world class to it as well ##game over passed in here (try moving into update method isntead??)
button = Button(screen_width, screen_height)

#objects method call that is run in game loop, for the actual game to run
def Objects(game_over, screen, walrus_group, refresh, flag_group, level_num):
     world.draw(screen) #passed in screen here to connect it to the World class for draw() method
     game_over, level_num = player.update(screen, walrus_group, game_over, refresh, flag_group, level_num) #calling player class update function  ##passing in walrus_group for collsion for game over event ###game_over retunred value and updates game_over value here
     walrus_group.draw(screen) #even though enemy class, walrus_group called since this is the object
     flag_group.draw(screen)
     return game_over, level_num


run = True
while run:
    print("level no: " + str(level_num) + " engame: " + str(end_game) + " begin: " + str(begin) + " try again: " +str(try_again) + " game over: " +str(game_over))
    #print("game over: " + str(game_over) + " refresh: " + str(refresh))

    clock.tick(fps)
    screen.fill((200,250,200))
    #screen.blit(character, (0,0))
    if begin == 0:
         begin_condition = button.start_update(screen, begin) #IF I WANTED TO ADD AN EXIT BUTTON, BUT CBA, THEN DO: run = False when exit button is clicked == True
         if begin_condition == 1:
              begin = 1

    #draw_grid()

    if game_over == 0 and begin == 1:
        walrus_group.update(screen) #walrus freeze in motion when game is over

    #player touches the flag
    if game_over == 2: #player 'wins'
         world_data = []
         world, level_num, end_game = reset_level(level_num, end_game)

         if end_game == 1:
              try_again = button.game_won(screen, try_again)
         game_over = 0
         #Objects(game_over, screen, walrus_group, refresh, flag_group, level_num)
    
    if begin == 1 and end_game == 0: #start button pressed
        game_over, level_num = Objects(game_over, screen, walrus_group, refresh, flag_group, level_num)
        #print("gameover: " + str(game_over) + " level num: " + str(level_num))

    if end_game == 1:
         walrus_group.empty() #still moving in background so removes
         try_again = button.game_won(screen, try_again)
         
         if try_again == 1:
            begin = 0
            end_game = 0
            try_again = 0
            player = player = Player(200, screen_height - 180, world)
            level_num = 0
            #world_gen(level_num)
            world, level_num, end_game = reset_level(level_num, end_game)

    if game_over == 1:
         refresh = button.update(screen, refresh) #when palyer hits walrus the restart button appears, which also returns the refresh value
         if refresh == 1 and end_game == 0:
              game_over = 0
              Objects(game_over, screen, walrus_group, refresh, flag_group, level_num)
              refresh = 0 #stops from refresh value being constantly called and constantly teleporting player to spawn coords
         

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()








#OLD way of loading in world
'''       
world_data = [
      
      [1, 1, 1, 1, 1],
      [1, 3, 0, 0, 1],
      [1, 2, 0, 3, 1],
      [1, 0, 0, 2, 1],
      [1, 2, 2, 1, 1],
]
'''