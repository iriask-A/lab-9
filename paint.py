import pygame
pygame.init()
#screen settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#list of colors for drawing
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]
#cell paramener for colors
COLOR_BUTTONS = [(10 + i * 40, 10, 30, 30) for i in range(len(COLORS))]
#shape types
SHAPES = ["draw", "rect", "circle", "square", "right triangle", "equilateral triangle","eraser"]
#cell parameters for shapes
SHAPE_BUTTONS = [(200 + i * 80, 10, 70, 50) for i in range(len(SHAPES))]
#set default color,mode,position
current_color = BLACK
mode = "draw"
start_pos = None
last_pos = None
brush_size = 5

#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

def drawing():
    #draw cells for colors and color them
    for i, rect in enumerate(COLOR_BUTTONS):
        pygame.draw.rect(screen, COLORS[i], rect)
    #draw cells for shpes and color them to grey color
    for i, rect in enumerate(SHAPE_BUTTONS):
        pygame.draw.rect(screen, (210, 200, 200), rect)
    #set all shapes and color them to black exept eraser
    for i in SHAPES:
        if i == "draw":
            pygame.draw.circle(screen,(0,0,0),(238,35), 10)
        elif i == "rect":
            pygame.draw.rect(screen,(0,0,0),(285,15,60,40))
        elif i == "circle":
            pygame.draw.circle(screen,(0,0,0),(395,35),20)
        elif i == "square":
            pygame.draw.rect(screen,(0,0,0),(455,15,40,40))
        elif i == "right triangle":
            pygame.draw.polygon(screen,(0,0,0),[[535,15],[535,55],[575,55]])
        elif i == "equilateral triangle":
            pygame.draw.polygon(screen,(0,0,0),[[635,15],[605,55],[665,55]])
        elif i == "eraser":
            pygame.draw.rect(screen,(255,255,255),(685,15,60,40))

#screen
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    #draw the menu
    drawing()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #takes positions of starting point
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            #saves the chosen color
            for i, rect in enumerate(COLOR_BUTTONS):
                if pygame.Rect(rect).collidepoint(x, y):
                    current_color = COLORS[i]
            #saves the chosen shape
            for i, rect in enumerate(SHAPE_BUTTONS):
                if pygame.Rect(rect).collidepoint(x, y):
                    mode = SHAPES[i]
            #save the start position
            start_pos = event.pos
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            #saves the end position
            end_pos = event.pos
            #settings for drawing each shape
            if mode == "square":
                pygame.draw.rect(canvas, current_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[0] - start_pos[0])))
            elif mode == "rect":
                pygame.draw.rect(canvas, current_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(canvas, current_color, start_pos, radius)
            elif mode == "right triangle":
                pygame.draw.polygon(canvas,current_color,[start_pos,end_pos,[start_pos[0],end_pos[1]]])
            elif mode == "equilateral triangle":
                pygame.draw.polygon(canvas,current_color,[start_pos,end_pos,[(2*start_pos[0]-end_pos[0]),end_pos[1]]])
        #settings for eraser and draw mode
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "draw":
                pygame.draw.line(canvas, current_color, last_pos, event.pos, 12)
                pygame.draw.circle(canvas, current_color, event.pos, 5)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.circle(canvas, WHITE, event.pos, 5)
                pygame.draw.line(canvas, WHITE, last_pos, event.pos, 12)
                last_pos = event.pos
    
    pygame.display.flip()

pygame.quit()
