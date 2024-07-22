import pygame as py
import random

py.init()
py.font.init()  #initalizes fonts and sfx, but i don't think font.init() is neccessary since it was working without it?
py.mixer.init()

screen_width = 1280
screen_height = 720
screen = py.display.set_mode((screen_width , screen_height))
background = py.transform.scale(py.image.load('Pong_background.png'), (1280,720))

hit_sfx = py.mixer.Sound('pop_sfx.mp3')

#circle and paddle pos
c_x = screen_width / 2
c_y = screen_height / 2

p1_x = 50
p1_y = screen_height / 2

p2_x = screen_width - 50-25
p2_y = screen_height /2 - 175

#declaring these varibales in global scope
random_number_x = 1
random_number_y = 1

#paddle controls
def paddle_controls(p1_y, p2_y, key):

    #paddle 1
    if key[py.K_w] == True and paddle_1.y > 0:
        p1_y -= 10

    elif key[py.K_s] == True and paddle_1.y < screen_height - 175:
        p1_y += 10

    #paddle 2
    if key[py.K_UP] == True and paddle_2.y > 0:
        p2_y -= 10

    elif key[py.K_DOWN] == True and paddle_2.y < screen_height - 175:
        p2_y += 10

    elif key[py.K_o] == True and paddle_2.y > 0:
        p2_y -= 10

    elif key[py.K_l] == True and paddle_2.y < screen_height - 175:
        p2_y += 10

    return p1_y , p2_y

#creates a random starting direction for ball
def starting_pos(random_number_x , random_number_y):
    negative_selector = str(random.randint(1,4))
    print("neg: " +negative_selector) #debug purpose

    if negative_selector == '1':
        random_number_x = round(random.random() ,5)* -10
        random_number_y = round(random.random() ,5)* -10

    elif negative_selector == '2':
        random_number_x = round(random.random() ,5)* -10
        random_number_y = round(random.random() ,5)* 10

    elif negative_selector == '3':
        random_number_x = round(random.random() ,5)* 10
        random_number_y = round(random.random(),5)* -10

    else:
        random_number_x = round(random.random() ,5)* 10
        random_number_y = round(random.random() ,5)* 10

    return random_number_x *2 , random_number_y *2

random_number_x , random_number_y = starting_pos(random_number_x , random_number_y) #this catches the returned variables, before it wasn't able to retrieve new values taht were returned and using the original set values

print(random_number_x) #debug purpose
print(random_number_y) #debug purpose

#points
paddle_1_points = 0
paddle_2_points = 0

#points text/font
paddle_font = py.font.SysFont('comicsans' , 30)

paddle_1_text = paddle_font.render("Points: " + str(paddle_1_points) , 1 , (255,255,255))
paddle_2_text = paddle_font.render("Points: " + str(paddle_2_points) , 1 , (255,255,255))

#sets ball speed/direction
vel = [random_number_x,random_number_y]
acceleration = 2

#fps
fps = 60
clock = py.time.Clock()

run = True
while run:
    clock.tick(fps)

    #screen.fill((0,0,0)) #original just plain black background but been updated with a simple image i made :)
    screen.blit(background , (0,0))
    screen.blit(paddle_1_text, (10 , 10))
    screen.blit(paddle_2_text, (1280 - 130 , 10))

    #in loop so points actually get updated
    paddle_1_text = paddle_font.render("Points: " + str(paddle_1_points) , 1 , (255,255,255))
    paddle_2_text = paddle_font.render("Points: " + str(paddle_2_points) , 1 , (255,255,255))

    key = py.key.get_pressed()
    p1_y, p2_y = paddle_controls(p1_y, p2_y, key)

    #ball object and 2 paddles
    ball = py.draw.circle(screen , (255,255,255) , (int(c_x) , int(c_y)) , 30)
    paddle_1 = py.draw.rect(screen , (255,255,255) , (p1_x , p1_y - 175 , 25 , 175))
    paddle_2 = py.draw.rect(screen , (255,255,255) , (p2_x , p2_y , 25 , 175))

    #paddle and ball collision
    if paddle_1.colliderect(ball):
        c_x = p1_x + 25 + 30 #stops paddle clipping with ball, remove this and u may see a weird bug when the ball touches the top of the paddle
        vel[1] += acceleration
        vel[0] = -vel[0]
        hit_sfx.play()

    if paddle_2.colliderect(ball):
        c_x = p2_x - 25 - 30
        vel[0] += acceleration
        vel[0] = -vel[0]
        hit_sfx.play()
    
    c_x += vel[0]
    c_y += vel[1]
    
    if c_x > screen_width - 30:
        #vel[0] += acceleration
        paddle_1_points += 1 #updates points value
        c_x = screen_width / 2
        c_y = screen_height / 2
        random_number_x , random_number_y = starting_pos(random_number_x , random_number_y) #creates a new random starting position when a ball has been conceded, also i mulitlped by a bit cause ball is quite slow sometimes :/
        vel[0] = random_number_x
        vel[1] = random_number_y
    
    elif c_x < 30:
        #vel[0] += acceleration
        paddle_2_points += 1
        c_x = screen_width / 2
        c_y = screen_height / 2
        random_number_x , random_number_y = starting_pos(random_number_x , random_number_y)
        vel[0] = random_number_x
        vel[1] = random_number_y

    elif c_y < 30:
        #vel[1] += acceleration
        vel[1] = -vel[1] #these lines allow the bounce of the ball when it hits the wall
        
    elif c_y > screen_height - 30:
        #vel[1] += acceleration
        vel[1] = -vel[1]

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    py.display.update()


### NEXT TIME IMRPOVEMENTS ###
#next time include a main function and also more functions for readablity


