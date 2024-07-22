import pygame as py
import random

#ALSO F*** YEAH, NO F***ING OBJECTS HERE (i think but yh p sure mf, but a yt vid with objects did help lol xd) completed: 22/07/2024 00:53 (i have wrk tmrw, i think)
#next time add fps hehe, little too happy of this project xD

py.init()

screen_width = 1280
screen_height = 720
screen = py.display.set_mode((screen_width , screen_height))

#circle pos
c_x = screen_width / 2
c_y = screen_height / 2

negative_selector = str(random.randint(1,4)) #for some reason print statement wants a string value
print("neg: " +negative_selector) #debug purpose

if negative_selector == '1':
    random_number_x = round(random.random() ,5)* -1
    random_number_y = round(random.random() ,5)* -1

elif negative_selector == '2':
    random_number_x = round(random.random() ,5)* -1
    random_number_y = round(random.random() ,5)

elif negative_selector == '3':
    random_number_x = round(random.random() ,5)
    random_number_y = round(random.random(),5)* -1

else:
    random_number_x = round(random.random() ,5)
    random_number_y = round(random.random() ,5)
  

print(random_number_x) #debug purpose
print(random_number_y) #debug purpose
#sets ball speed, but rly it is just how many pixels it moves per loop, so 1 means 1 pixel movement in whatever direction
vel = [random_number_x,random_number_y]


run = True
while run:

    screen.fill((0,0,0)) #refreshes screen, if removed you can see the path of ball, can be commented out for debug purposes too
                          #also kinda showed that ball path isn't that super random :/, now it is, well it is more random, not true random but whatevs...
    random_number_x = round(random.random() ,5) #this and below might not be neccessary
    random_number_y = round(random.random() ,5)
    print("x " + str(random_number_x) + " and y " + str(random_number_y) ) #debug purpose

    #ball object (idk if it is an object), its not exactly i think
    ball = py.draw.circle(screen , (255,255,255) , (int(c_x) , int(c_y)) , 30)

    c_x += vel[0]
    c_y += vel[1]
    
    if c_x > screen_width - 30:
        vel[0] = random_number_x = round(random.random() ,5) #made it more random, its not perfect p sure but cba to paly with this anymore ITS WORKING NOW, mayb 
                                                             #dont make ball so slow but yh other than that THIS IS FINE,PLEASE VOICES IN MY HEAD STAWP
        vel[0] = -vel[0]

    elif c_x < 30:
        vel[0] = random_number_x = round(random.random() ,5) * -1
        vel[0] = -vel[0]

    elif c_y < 30:
        vel[1] = random_number_x = round(random.random() ,5) * -1
        vel[1] = -vel[1] #these lines allow the bounce of the ball when it hits the wall
        
    elif c_y > screen_height - 30:
        vel[1] = random_number_x = round(random.random() ,5)
        vel[1] = -vel[1]

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    py.display.update()
    




#PREVIOUS MISTAKES AND OLD CODE N WHATNOT#

#vel = 1 #instead of a variable, used an array to hold to values so 2 diff velocity values can be had for the ball at the x and y therefore allowing it to acc move arnd

#c_x += 1 #introduced vel variable (velocity) since it is in a loop it kept on resetting back to this instead of chaning direction!

'''
    #up
    if random_direction == 1 and ball.y > 0:
         c_y -= 1

    #down
    if random_direction == 2 and ball.y < 720-60:
         c_y += 1

    #left
    if random_direction == 3 and ball.x > 0:
         c_x -= 1

    #right
    if random_direction == 4 and ball.x < 1280-60:
        c_x += 1
'''
    

'''
    #down
    if random_direction == 2:
         c_y += 1
    if random_direction == 2 and ball.y > 720-30:
         random_direction = random.randint(1,4)

    #left
    if random_direction == 3:
         c_x += 1
    if random_direction == 3 and ball.x > 1280:
         random_direction = random.randint(1,4)

    #right
    if random_direction == 4:
         c_x += 1
    if random_direction == 4 and ball.x > 0:
         random_direction = random.randint(1,4)

'''

#old code for tryna get a direction, failed terribly, i think but p sure it did
'''
random_direction = 4
def direction():
    random_direction = random.randint(1,4)

    #print(random_direction) #debug stuff

'''

#just didnt rly need this:
#random variables
#random_number_x = 0
#random_number_y = 0

