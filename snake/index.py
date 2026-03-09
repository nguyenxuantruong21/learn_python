import pygame
from time import sleep
from random import randint

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display .set_caption('Snake')
running = True
GREEN = (0,200,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
clock = pygame.time.Clock()

# snakes: tail - head
snakes = [[5,10],[5,11]]
direction = "right"
apple = [randint(0,19),randint(0,19)]
font_small = pygame.font.SysFont('sans',20)
font_big = pygame.font.SysFont('sans',50)
score = 0
pausing = False

while running:
    clock.tick(60)
    screen.fill(BLACK)
    
    tail_x = snakes[0][0]
    tail_y = snakes[0][1]

    # Draw grid
    for i in range(20):
        pygame.draw.line(screen, WHITE, (0,i*30), (600,i*30))
        pygame.draw.line(screen, WHITE, (i*30,0), (i*30,600))

    # Draw snake
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))

    # Draw apple
    pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

    # Point
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0,[tail_x,tail_y]) 
        apple = [randint(0,19),randint(0,19)]
        score += 1  
         
    # check crash with edge
    if snakes[-1][0] < 0 or snakes[1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1]>19:
        pausing = True
    
    # check crash with body
    for i in range(len(snakes)-1):
        if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
            pausing = True      


    # Draw game over
    if  pausing:
        game_over_text = font_big.render('Game over, score ' + str(score), True, WHITE)
        pres_space_text = font_big.render('Press Space to continue', True, WHITE)
        screen.blit(game_over_text, (50,200))
        screen.blit(pres_space_text, (50,300))


    # Draw score
    score_text = font_small.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text,(5,5))

    # Direction
    if pausing == False: 
        if direction == 'right':
            snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
            snakes.pop(0)
        
        if direction == 'left':
            snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
            snakes.pop(0)

        if direction == 'up':
            snakes.append([snakes[-1][0], snakes[-1][1] - 1])
            snakes.pop(0)
        
        if direction == 'down':
            snakes.append([snakes[-1][0], snakes[-1][1] + 1])
            snakes.pop(0)

    sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # append head - remove tail
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
              direction = 'up'
               
            if event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            
            if event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            
            if event.key == pygame.K_SPACE and pausing == True:
                pausing = False
                snakes = [[5,10],[5,11]]
                apple = [randint(0,19),randint(0,19)]

    pygame.display.flip()


pygame.quit()