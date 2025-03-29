import pygame
import random
import cv2
import numpy as np

# Настройки
width, height = 640, 480
cell_size = 20

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Создаем файл для видеозаписи
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('snake_game.avi', fourcc, 30.0, (width, height))


# Класс для змейки
class Snake:
    def __init__(self):
        self.body = [[100, 100], [80, 100], [60, 100]]  # Начальное положение змейки
        self.direction = 'RIGHT'
        self.grow = False

    def move(self):
        head = self.body[0][:]
        if self.direction == 'UP':
            head[1] -= cell_size
        elif self.direction == 'DOWN':
            head[1] += cell_size
        elif self.direction == 'LEFT':
            head[0] -= cell_size
        elif self.direction == 'RIGHT':
            head[0] += cell_size

        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

            # Класс для змейки
            class Snake:
                def __init__(self):
                    self.body = [[100, 100], [80, 100], [60, 100]]  # Начальное положение змейки
                    self.direction = 'RIGHT'
                    self.grow = False

                def move(self):
                    head = self.body[0][:]
                    if self.direction == 'UP':
                        head[1] -= cell_size
                    elif self.direction == 'DOWN':
                        head[1] += cell_size
                    elif self.direction == 'LEFT':
                        head[0] -= cell_size
                    elif self.direction == 'RIGHT':
                        head[0] += cell_size

                    self.body.insert(0, head)
                    if not self.grow:
                        self.body.pop()
                    else:
                        self.grow = False
                        Основная
                        функция

                    def game_loop():
                        snake = Snake()
                        food_position = [random.randrange(1, width // cell_size) * cell_size,
                                         random.randrange(1, height // cell_size) * cell_size]
                        game_over = False

                        while not game_over:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    game_over = True
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP and snake.direction != 'DOWN':
                                        snake.direction = 'UP'
                                    if event.key == pygame.K_DOWN and snake.direction != 'UP':
                                        snake.direction = 'DOWN'
                                    if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                                        snake.direction = 'LEFT'
                                    if event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                                        snake.direction = 'RIGHT'

                            snake.move()

                            if snake.body[0] == food_position:
                                snake.grow_snake()
                                food_position = [random.randrange(1, width // cell_size) * cell_size,
                                                 random.randrange(1, height // cell_size) * cell_size]

                            screen.fill(black)
                            pygame.draw.rect(screen, green, (food_position[0], food_position[1], cell_size, cell_size))
                            for segment in snake.body:
                                pygame.draw.rect(screen, white, (segment[0], segment[1], cell_size, cell_size))

                            # Запись текущего кадра в видео
                            frame = pygame.surfarray.array3d(pygame.display.get_surface())
                            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                            out.write(frame)

                            pygame.display.flip()
                            clock.tick(10)

                        out.release()
                        pygame.quit()

                    if __name__ == "__main__":
                        game_loop()



