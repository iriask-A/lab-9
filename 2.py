import pygame
import random,math

#colors
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


pygame.init()
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#fonts
font_style = pygame.font.SysFont("Verdana", 20)

def print_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def generate_food(snake_list):
    while True:
        food_type = random.choice(food_types)
        food_x = random.randrange(0, width - snake_block, snake_block)
        food_y = random.randrange(0, height - snake_block, snake_block)
        if [food_x, food_y] not in snake_list:
            return food_x, food_y

running = True
x1, y1 = width / 2, height / 2
x1_change, y1_change = 0, 0
snake_list = []
snake_length = 1
speed = 10
score = 0
level = 1
food_x, food_y = generate_food(snake_list)
food_type = generate_food(food_types)

while running:
    display.fill(blue)
    if food_type == "red_food":
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])
    elif food_type == "yellow_food":
        pygame.draw.rect(display, yellow, [food_x, food_y, snake_block, snake_block])
    elif food_type == "green_food":
        pygame.draw.rect(display, yellow, [food_x, food_y, snake_block, snake_block])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change, y1_change = -snake_block, 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change, y1_change = snake_block, 0
            elif event.key == pygame.K_UP and y1_change == 0:
                x1_change, y1_change = 0, -snake_block
            elif event.key == pygame.K_DOWN and y1_change == 0:
                x1_change, y1_change = 0, snake_block

    x1 += x1_change
    y1 += y1_change

    #border_check
    if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height:
        running = False

    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    if snake_head in snake_list[:-1]:
        running = False

    print_snake(snake_block, snake_list)

    #check for eating food
    if x1 == food_x and y1 == food_y:
        if food_type == "red_food":
            score += 1
        elif food_type == "yellow_food":
            score += 2
        elif food_type == "green_food":
            score += 3
        snake_length += 1
        food_x, food_y = generate_food(snake_list)
        if math.ceil(score % 3) != new_score:
            level += 1
            speed += 2
            new_score = math.ceil(score % 3)

    #score
    score_text = font_style.render(f"Score: {score}  Level: {level}", True, white)
    display.blit(score_text, [10, 10])

    pygame.display.update()
    clock.tick(speed)

pygame.quit()

