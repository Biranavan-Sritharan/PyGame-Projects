import pygame as py 

#initalizes pygame,you just need it ok!
py.init()
py.font.init()  #initalizes fonts to game for win message and health left for rectangles
py.mixer.init() #initalizes sound/music to game

#sfx set up
fire_sfx = py.mixer.Sound('quack_sfx.mp3')

#sets font of text for health
hp_font = py.font.SysFont('comicsans' , 30)
win_font = py.font.SysFont('comicsans' , 100)

screen = py.display.set_mode((1280, 720))
background = py.transform.scale(py.image.load('background.png'), (1280,720)) #original image size is 1920x1080, it has been loaded in AND scaled down to 1280x720

#this sets title of window and icon
py.display.set_caption("First pygame :)")

icon = py.image.load('icon_n_asset.png')
py.display.set_icon(icon)

#creates rectangle position (x,y) and size
rectangle = py.Rect((300,300,90,90))  
other_rectangle = py.Rect((700,300,90,90))

border = py.Rect((630,0,10,720))

#bullet attributes, is it an object? bullet that is
bullet_speed = 12
max_bullet = 5
bullet_delay = 250

#hit 
rect_hit = py.USEREVENT + 1  #creates 2 unique events, this is used for when bullet hit either rectangle
other_hit = py.USEREVENT + 2

#bullet collisons,removal and movement function
def handle(rectangle,other_rectangle,rect_bullets,other_bullets):
    
    for bullet in rect_bullets:
        bullet.x += bullet_speed  #sets speed/movement of bullet

        for event in py.event.get():  #trying to remove any lingering bullets after game finishes but not working, (not added for other_rect)
            if event.type == 1:
                rect_bullets.remove(bullet)

        if other_rectangle.colliderect(bullet):  #detects collison of rectangle with bullet, collison detected with other_rectangle and bullet NOT the rectangle bullet is fired from!
            py.event.post(py.event.Event(rect_hit))  #creates event where rectangle is hit with bullet
            rect_bullets.remove(bullet)  #bullet fired from rect is removed
        elif bullet.x > 1280:  #if bullet goes off-screen then the bullet is also removed
            rect_bullets.remove(bullet)    

    for bullet in other_bullets:
        bullet.x -= bullet_speed  
        if rectangle.colliderect(bullet):  
            py.event.post(py.event.Event(other_hit))  #this .post, sends an event of hit to the for loop that retreives the events?, the for loop that contains py.quit()
            other_bullets.remove(bullet) 
        elif bullet.x < 0:
            other_bullets.remove(bullet)


#game loop within main function
def main():

    fps = 60
    clock = py.time.Clock()

    #bullets array, see if this can be shortned down to just one list later on
    rect_bullets = []
    other_bullets = []

    #sets health of rectangles
    rect_hp = 5
    other_hp = 5

    #sets up/initialises bullet delay variables
    rect_last_time = 0
    other_last_time = 0

    run = True
    while run:

        clock.tick(fps)

        #sets background
        #screen.fill((0,0,0)) #when rectangle moves it leaves trail, this makes it that 
                            #when rect is moved the trail is not there BECAUSE the screen is constantly refreshed 
                            #with this background which in this case has been set to black
        screen.blit(background , (0,0))  #add custom background that is constantly refreshed, replaced the screen.fill line above
                                         #blit method is used to just add an image to the surface of the window

        #puts rectangles on screen
        py.draw.rect(screen, (255,0,0), rectangle)  
        py.draw.rect(screen, (0,255,0), other_rectangle)
        py.draw.rect(screen, (50,50,50) , border)
        #py.draw.circle(screen , (0,0,255) , (500,500) , 10) #for now this will be commented out but added in later

        #drawing bullets to screen
        for bullet in rect_bullets:
            py.draw.rect(screen , (255,255,0) , bullet)

        for bullet in other_bullets:
            py.draw.rect(screen , (255,255,0) , bullet)

        #health values linked to a font and will be displayed under a var which is displayed to the screen
        rect_hp_txt = hp_font.render("Health: " + str(rect_hp) , 1 , (255,255,255)) #str converts the int into a string to be displayed on screen
        other_hp_txt = hp_font.render("Health: " + str(other_hp) , 1, (255,255,255)) #also the 1 is anti-analsing and also colour of text is set

        screen.blit(rect_hp_txt , (10,10))
        screen.blit(other_hp_txt , (1280 - 140,10))
        
        #controls, can chuck these in a function later on
        key = py.key.get_pressed()

        #for red rectangle
        if key[py.K_w] == True and rectangle.y > 0: #the and rectangle.y > 0 is creates the boundary and stops rectangle goin past into the negative coords
            rectangle.move_ip(0,-8)  #ip in move_ip means move in place

        elif key[py.K_s] == True and rectangle.y < 630: #so here the size of rectangle needs to be accounted for, rect has size of 90 so 720(win size) - 90 = 63
            rectangle.move_ip(0,8)                      #so we dont want our rectangle goin past 630

        elif key[py.K_a] == True and rectangle.x > 0:
            rectangle.move_ip(-8,0)

        elif key[py.K_d] == True and rectangle.x < 630-90: #lazy to do 1280-90. but same applies with rest of code, not too sure what to do if i decide to change screen size but oh well
            rectangle.move_ip(8,0)                          #but prolly along the lines of creating some kinda of object to have collisions with???

        #for green rectangle
        if key[py.K_UP] == True and other_rectangle.y > 0:
            other_rectangle.y -= 8  #using .x and .y is a in-built method from pygame calling from the x and y values when the objects were made
                                    #alternate to move_ip, i guess
        elif key[py.K_DOWN] == True and other_rectangle.y < 630:
            other_rectangle.y += 8

        elif key[py.K_LEFT] == True and other_rectangle.x > border.x+10: #also just want to stop rectangle going past border so border x coord obtained and +10 to account for border size, otherwise small overlap occurs
            other_rectangle.x -= 8

        elif key[py.K_RIGHT] == True and other_rectangle.x < 1280-90:
            other_rectangle.x += 8

        #this loop here prevents the screen from closing immedietly until I quit myself
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                py.quit() #if you remove this line, you can't actaully quit the game by clicking X button, lol

            #bullet activation, delay and spawn placement
            if event.type == py.KEYDOWN:  #tells computer that when a key is pressed downward
                current_time = py.time.get_ticks()
                if event.key == py.K_LCTRL and len(rect_bullets) < max_bullet:  #the 'len(rect_bullets) < max_bullet' checks how many bullets on screen and does let you fire till those bullets are gone
                    if current_time - rect_last_time > bullet_delay:
                        bullet = py.Rect(rectangle.x + rectangle.width, rectangle.y + (rectangle.height//2) , 10 , 5)  #rect.width needs to be added here potentially
                        rect_bullets.append(bullet) #bullet is added to list
                        fire_sfx.play()
                        rect_last_time = current_time

                if event.key == py.K_RCTRL and len(other_bullets) < max_bullet:
                    if current_time - other_last_time > bullet_delay:
                        bullet = py.Rect(other_rectangle.x - other_rectangle.width +90, other_rectangle.y + (other_rectangle.height//2) , 10 , 5)
                        other_bullets.append(bullet)
                        fire_sfx.play()
                        other_last_time = current_time

            print(rect_bullets, other_bullets) #shows bullets being appended and removed from array live in terminal as game runs

            if event.type == rect_hit:  #so from .post in handle() function, this if statement is listening for the rect_hit to be posted/ rect_hit event to be posted via .post
                other_hp -= 1

            if event.type == other_hit:
                rect_hp -= 1

        #sets the win message when one of the rectangles win
        win_msg = ""
        if rect_hp <= -1:
            win_msg = "Green Won!"
        
        if other_hp <=-1:
            win_msg = "Red Won!"

        if win_msg != "":  #so someone has won since the win_msg var has been updated, so this line is then run
            py.event.post(py.event.Event(1)) #post event to handle function where it is read. 
            rect_bullets = [] #resets the array to nothing
            other_bullets = []
            end_txt = win_font.render(win_msg , 1 , (255,255,255))
            screen.blit(end_txt , ((1280 / 2)  , (720 / 2)))           #fix these coords, not centerised
            py.display.update() #just makes it properly update
            py.time.delay(3000) #creates a delay before restarting game
            break #breaks from if and runs the main() again

        #bullet collisons,removal and movement function is called here
        handle(rectangle,other_rectangle,rect_bullets,other_bullets)

        py.display.update() #updates screen so red rect appears

    main() #when game ends, after 5 seconds from py.time.delay() ,the game will restart

#not exactly too clear on this, but just call main() when file is run, even as exe or something...
if __name__ == "__main__":
    main()





#--- OLD CODE / MISTAKES MADE ALONG THE WAY / AND BU-G FIXES :) ---#

'''
---NEXT TIME---
create an assets folder to store all assets, so with this import os would prolly happen as well
'''

#screen.fill((0,0,0))
#py.display.flip()

'''
#rectangle
red = (255,0,0)
circle = py.rect(70,200,40,100)
py.rect(screen, red, circle)
'''

#screen.blit(snake, (500,500))
#snake = py.image.load(os.path.join('PyGame','icon_n_assest.png'))

'''
Not sure if a sepeate library has to be installed, tick could not be found error appears, check it out later

#set fps to be at 60, so how many time a second (main game) while loop runs
fps = 60 
clock = py.tick.Clock()
clock.tick(fps)
'''

'''
Trying to get a circle to be drawn:
circle = py.Rect((500,500,50,50)) #as far as i can tell this isn't neccessary
py.draw.circl(screen , (0,0,255) , (500,500) , 20) #circle was mispelt
'''

'''
#fix bug where some bullets can linger to next round, perhaps with rect_bullets.remove(bullet)
                                                                   #other_bullets.remove(bullet)
#bug fixed by just clearing the array itself by declaring the list again in the win if block, .remove() didn't work since the bullet would
fire anyway since it was still loaded into the array and would fire immedieatly next round, discovered looking at the printed list in terminal :0

UPDATE: Bug acc not fixed still very much prevalent, tried adding a post and get event types but to no avail in the win != "" area and also handle function (in a for loop)
'''

'''
Not a great fix but lives end on -1 lives, since the delay and freeze n whatnot makes it freeze on 1 and it just looked weird, not a great bug fix but 
oh well :/
'''