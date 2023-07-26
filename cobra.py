//Code

import pygame
import random
pygame.init()
#background color is black
background = (0,0,0)
# cobra color
grey = (255,165,0)
# random food color
food = (255,0,166)
screen_width  = 900
screen_height = 900
window_of_the_game = pygame.display.set_mode(screen_width,screen_height)

pygame.display.set_caption("Rizan World")
pygame.display.update()
time = pygame.time.Clock()
font = pygame.font.SysFont(None,500)

def text_screen(text,color,x,y):
    
    #render is used to display the object on the screen
    screen_text=font.render(text,True,color)
    #blit is a method that is used to copy an image or part of an image to another image or surface
    window_of_the_game.blit(screen_text,[x,y])

def plot_snake_game(color,window_of_the_game,list_of_the_snake,size_of_the_snake):
    for x,y in list_of_the_snake:
        pygame.draw.polygon(window_of_the_game,color,size_of_the_snake)
        
def gameloop():
    exit_game = False
    game_over=False
    snake_x =  45
    velocity_x=0
    velocity_y=0
    snake_list=1
    
    food_x=random.randint(20,screen_width-20)
    food_y=random.randint(60,screen_height-20)
    score=0
    init_velocity = 4
    snake_size=30
    fps=60
    while not exit_game:
        if game_over:
            window_of_the_game.fill(background)
            text_screen("Game Over!, Dont worry you can try next time, Just don't loose hope",(255,0,0),55,250)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity()
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                        snake_x=snake_x + velocity_x
                        snake_y=snake_y + velocity_y
                            
                    if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                        score +=1
                        food_x=random.randint(20,screen_width-30)
                        food_y=random.randint(60,screen_height-30)
                        snk_length +=5
                        window_of_the_game.fill(background)
                        text_screen("Score: " + str(score*10),food, 5, 5)
                        pygame.draw.rect(window_of_the_game,food,[food_x,food_y,snake_size,snake_size])
                        pygame.draw.line(window_of_the_game,food,(0,40),(900,40),5)
                        head = []
                        head.append(snake_x)
                        head.append(snake_y)
                        snake_list.append(head)
                        if len(snake_list)>snk_length:
                            del snake_list[0]
                        if head in snake_list[:-1]:
                            game_over=True
                        if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                            game_over = True
            plot_snake_game(window_of_the_game, grey, snake_list, snake_size)
        pygame.display.update()
        time.tick(fps)
    pygame.quit()
    quit()
gameloop

