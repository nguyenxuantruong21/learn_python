import pygame
from random import randint

# Cấu hình hằng số
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 30
GRID_COUNT = WIDTH // GRID_SIZE
FPS = 10 # Thay vì dùng sleep(0.1), ta dùng FPS thấp để rắn chạy chậm

# Màu sắc
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [[5, 10], [6, 10]] # [x, y]
        self.direction = "right"

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def move(self):
        head_x, head_y = self.body[-1]
        
        if self.direction == 'up': head_y -= 1
        elif self.direction == 'down': head_y += 1
        elif self.direction == 'left': head_x -= 1
        elif self.direction == 'right': head_x += 1
        
        self.body.append([head_x, head_y])
        self.body.pop(0)

    def grow(self):
        # Thêm một đốt dựa trên vị trí đuôi hiện tại
        self.body.insert(0, list(self.body[0]))

class Apple:
    def __init__(self):
        self.randomize()

    def randomize(self):
        self.pos = [randint(0, GRID_COUNT - 1), randint(0, GRID_COUNT - 1)]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.pos[0] * GRID_SIZE, self.pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake OOP Version')
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
        
        # Đâm vào tường
        if head[0] < 0 or head[0] >= GRID_COUNT or head[1] < 0 or head[1] >= GRID_COUNT:
            self.pausing = True
        
        # Tự cắn mình
        if head in self.snake.body[:-1]:
            self.pausing = True

        # Ăn táo
        if head == self.apple.pos:
            self.snake.grow()
            self.apple.randomize()
            self.score += 1

    def draw_grid(self):
        for i in range(GRID_COUNT):
            pygame.draw.line(self.screen, (40, 40, 40), (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE))
            pygame.draw.line(self.screen, (40, 40, 40), (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT))

    def run(self):
        while self.running:
            self.screen.fill(BLACK)
            self.draw_grid()

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
                    
                    if event.key == pygame.K_SPACE and self.pausing:
                        self.reset()

            if not self.pausing:
                self.snake.move()
                self.check_collision()
                self.snake.draw(self.screen)
                self.apple.draw(self.screen)
            else:
                msg = self.font_big.render(f'Game Over! Score: {self.score}', True, WHITE)
                retry = self.font_small.render('Press Space to Restart', True, WHITE)
                self.screen.blit(msg, (150, 250))
                self.screen.blit(retry, (200, 320))

            score_txt = self.font_small.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_txt, (10, 10))

            pygame.display.flip()
            self.clock.tick(FPS) # Kiểm soát tốc độ game chuẩn hơn sleep()

        pygame.quit()

# Chạy game
if __name__ == "__main__":
    my_game = Game()
    my_game.run()