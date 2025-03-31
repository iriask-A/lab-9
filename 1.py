import pygame
from pygame.locals import *
import random, time
pygame.init()

FPS = 60
clock = pygame.time.Clock()
width = 400
height = 600
speed = 5
enemy_speed = 5
score = 0
coins_collected = 0
new_coins_collected = coins_collected
#load the enemy image
enemy = pygame.image.load("images/enemy.png")
#change the size of enemy
enemy = pygame.transform.scale(enemy, (60, 80))
#same for player
player = pygame.image.load("images/player.png")
#rotated the player image to 180 degrees
player = pygame.transform.rotate(player, 180)
player = pygame.transform.scale(player, (60, 80))
#same for coin image
coin_img = pygame.image.load("images/coin.png")
#removed the white background
coin_img.set_colorkey((255,255,255))
#created 3 types of coins by changind the size
coin_img = pygame.transform.scale(coin_img, (30, 30))
coin_bigger = pygame.transform.scale(coin_img, (40, 40))
coin_biggest = pygame.transform.scale(coin_img, (50, 50))
#font for game over text
font = pygame.font.SysFont("Verdana", 60)
#font for coins,levels text
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))
#added background image and aligned to the screen size
background = pygame.image.load("images/road.png")
background = pygame.transform.scale(background, (width, height))
#created a screen and colored into white
screen = pygame.display.set_mode((400, 600))
screen.fill((255, 255, 255))
#named the game
pygame.display.set_caption("Racer")

# enemy's class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
        self.enemy_speed = 5

    def move(self):
        global score
        self.rect.move_ip(0, self.enemy_speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

# player's class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < width and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# coin1 class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), random.randint(100, 500))

    def move(self):
        self.rect.move_ip(0, speed // 2)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
# coin2 class
class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_bigger
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), random.randint(100, 500))

    def move(self):
        self.rect.move_ip(0, speed // 2)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
# coin3 class
class Coin3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_biggest
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), random.randint(100, 500))

    def move(self):
        self.rect.move_ip(0, speed // 2)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()
C3 = Coin3()
list = [C1,C2,C3]
enemy = pygame.sprite.Group()
enemy.add(E1)

coin1 = pygame.sprite.Group()
coin1.add(C1)
coin2 = pygame.sprite.Group()
coin2.add(C2)
coin3 = pygame.sprite.Group()
coin3.add(C3)
coins = pygame.sprite.Group()
coins.add(coin1,coin2,coin3)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)

inc_speed= pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 3000)

game_start_time = time.time()
running = True
while running:
    #show everything on the screen
    screen.blit(background, (0, 0))
    scores = font_small.render(f"Score: {score}", True, (0, 0, 0))
    coins_text = font_small.render(f"Coins: {coins_collected}", True, (255, 215, 0))
    screen.blit(scores, (10, 10))
    screen.blit(coins_text, (width - 100, 10))
    for event in pygame.event.get():
        #increase the speed for each 10 coins collected
        if coins_collected >= new_coins_collected +10:
            enemy_speed += 0.5
            print(1)
            new_coins_collected = coins_collected
        #increase speed to 0,5 each 3 seconds
        if event.type == inc_speed:
            print(2)
            enemy_speed += 0.5
        #stop running the game if the quit button clicked
        if event.type == QUIT:
            running = False
    #make enemy and player move
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    #make 3 types of coins move
    for entity in coins:
        screen.blit(entity.image, entity.rect)
        entity.move()
    #stop the game if player touches the enemy
    if pygame.sprite.spritecollideany(P1, enemy):
        #turn the screen into red
        screen.fill((255, 0, 0))
        #show the game over text
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        #wait for 2 seconds and exit the game
        time.sleep(2)
        pygame.quit()
        sys.exit()
    #collect different type of coins
    if pygame.sprite.spritecollideany(P1,coins):
        for i in coins:
            if pygame.sprite.collide_rect(P1,i):
                if i in coin1:
                    coins_collected += 1
                elif i in coin2:
                    coins_collected += 2
                elif i in coin3:
                    coins_collected += 3
                #add a new coin on the screen if the player collects the coin
                i.rect.center = (random.randint(40, width - 40), 0)
             
    #update the screen   
    pygame.display.update()
    #update tyme per second
    clock.tick(FPS)
pygame.quit()