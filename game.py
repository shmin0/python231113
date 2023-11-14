# game 

# pip install pygame

import pygame
import sys

# 초기화
pygame.init()

# 게임 설정
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_RADIUS = 15
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 30
BLOCK_GAP = 10

# 색깔
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 시계 생성
clock = pygame.time.Clock()

# 초기 위치
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# 패들 생성
paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 생성
ball = pygame.Rect(ball_x, ball_y, BALL_RADIUS, BALL_RADIUS)

# 블록 생성
blocks = []
for row in range(3):
    for col in range(8):
        block = pygame.Rect(
            col * (BLOCK_WIDTH + BLOCK_GAP),
            row * (BLOCK_HEIGHT + BLOCK_GAP),
            BLOCK_WIDTH,
            BLOCK_HEIGHT,
        )
        blocks.append(block)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 7
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 7

    # 공 이동
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 벽과의 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과의 충돌
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # 블록과의 충돌
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 게임 오버 체크
    if ball.bottom >= HEIGHT:
        pygame.quit()
        sys.exit()

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    # 업데이트
    pygame.display.flip()
    clock.tick(60)