import pygame
from constants import *
from snake_apple import Snake, Apple

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake OOP - Separated Files')
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.SysFont('sans', 20)
        self.font_big = pygame.font.SysFont('sans', 40)
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.pausing = False
        self.running = True

    def check_collision(self):
        head = self.snake.body[-1]
        if head[0] < 0 or head[0] >= GRID_COUNT or head[1] < 0 or head[1] >= GRID_COUNT:
            self.pausing = True
        if head in self.snake.body[:-1]:
            self.pausing = True
        if head == self.apple.pos:
            self.snake.grow()
            self.apple.randomize()
            self.score += 1

    def draw_elements(self):
        self.screen.fill(BLACK)
        # Draw Grid
        for i in range(GRID_COUNT):
            pygame.draw.line(self.screen, DARK_GREY, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE))
            pygame.draw.line(self.screen, DARK_GREY, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT))
        
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
        
        # Draw Score
        score_txt = self.font_small.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_txt, (10, 10))

        if self.pausing:
            msg = self.font_big.render(f'GAME OVER! SCORE: {self.score}', True, WHITE)
            retry = self.font_small.render('Press Space to Restart', True, WHITE)
            self.screen.blit(msg, (120, 250))
            self.screen.blit(retry, (200, 320))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if not self.pausing:
                    if event.key == pygame.K_UP and self.snake.direction != 'down':
                        self.snake.direction = 'up'
                    elif event.key == pygame.K_DOWN and self.snake.direction != 'up':
                        self.snake.direction = 'down'
                    elif event.key == pygame.K_LEFT and self.snake.direction != 'right':
                        self.snake.direction = 'left'
                    elif event.key == pygame.K_RIGHT and self.snake.direction != 'left':
                        self.snake.direction = 'right'
                elif event.key == pygame.K_SPACE:
                    self.reset()

    def update(self):
        if not self.pausing:
            self.snake.move()
            self.check_collision()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw_elements()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()