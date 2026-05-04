import pygame
import random,math,time
pygame.init()

#colors and some needed variables
blue = (50, 153, 213)
black = (0, 0, 0)
red = (213, 50, 80)
yellow = (255, 255, 0)
green = (0, 255, 0)
white = (255, 255, 255)
new_score = 0
width = 600
height = 400
snake_block = 10
food_types = ["red_food", "green_food", "yellow_food"]

#creating the screen
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#fonts for levels and scores text
font_style = pygame.font.SysFont("Verdana", 20)
#print snake and further make it longer
def print_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])
#food generation with randomizer
def generate_food(snake_list):
    while True:
        food_type = random.choice(food_types)
        food_x = random.randrange(0, width - snake_block, snake_block)
        food_y = random.randrange(0, height - snake_block, snake_block)
        if [food_x, food_y] not in snake_list:
            return food_x, food_y, food_type
#other needed variables
running = True
x1, y1 = width / 2, height / 2
x1_change, y1_change = 0, 0
snake_list = []
snake_length = 1
speed = 10
#timers for disappearing of food after certain time
timer = pygame.USEREVENT + 1
time_active = False
visible = False
score = 0
level = 1
#took values from the function
food_x, food_y, food_type = generate_food(snake_list)

while running:
    display.fill(blue)
    #exit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #snake movement control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change, y1_change = -snake_block, 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change, y1_change = snake_block, 0
            elif event.key == pygame.K_UP and y1_change == 0:
                x1_change, y1_change = 0, -snake_block
            elif event.key == pygame.K_DOWN and y1_change == 0:
                x1_change, y1_change = 0, snake_block
        #setting timer
        if event.type == timer:
            visible = True
            time_active = False
            pygame.time.set_timer(timer,0)
    #create a food when the food is chosen
    if  not visible:
        if food_type == "red_food":
            pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])
        elif food_type == "yellow_food":
            pygame.draw.rect(display, yellow, [food_x, food_y, snake_block, snake_block])
        elif food_type == "green_food":
            pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])
        #set timer for 10 sec 
        if not time_active:
            pygame.time.set_timer(timer, 10000)  
            time_active = True
    #update snake position
    x1 += x1_change
    y1 += y1_change

    #border check
    if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height:
        running = False
    #assign snake head
    snake_head = [x1, y1]
    #add this coordinate to the end of snake body list
    snake_list.append(snake_head)
    #and removes the last element from list(for our case is first element in a list)
    if len(snake_list) > snake_length:
        del snake_list[0]
    #checks if snake does not hit itself
    if snake_head in snake_list[:-1]:
        running = False
    #draw snake
    print_snake(snake_block, snake_list)

    #check for eating food
    if x1 == food_x and y1 == food_y or  visible:
        visible = False
        #counting the scores
        if food_type == "red_food":
            score += 1
        elif food_type == "yellow_food":
            score += 2
        elif food_type == "green_food":
            score += 3
        snake_length += 1
        #generate another food
        food_x, food_y, food_type = generate_food(snake_list)
        time_active = False
        #upgrade the level and increase the speed 
        if score-3 >= new_score:
            level += 1
            speed += 2
            new_score = score
    #score
    #display score and level texts on the screen
    score_text = font_style.render(f"Score: {score}  Level: {level}", True, white)
    display.blit(score_text, [10, 10])

    pygame.display.update()
    clock.tick(speed)

pygame.quit()

