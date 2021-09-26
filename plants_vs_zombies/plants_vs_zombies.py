import pygame
import time

WIDTH = 360  # 游戏窗口的宽度
HEIGHT = 480 # 游戏窗口的高度
FPS = 30 # 帧率

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  #声音初始化
screen = pygame.display.set_mode((WIDTH, HEIGHT))       # 创建窗口
pygame.display.set_caption("My Game")#设置游戏窗口标题栏文字
clock = pygame.time.Clock()

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

count = 0
start = time.time()

# Game Loop
running = True
while running:




    # capture for pygame event
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False




    # Draw / render
    screen.fill(GREEN)

    my_font = pygame.font.Font(None, 60)
    text_image = my_font.render("pygame", True, WHITE)

    screen.blit(text_image, (10, 100))
    # pygame.display.flip()

    # keep loop running at the right speed
    clock.tick(FPS)
    # Update
    count += 1
    now = time.time()
    fps = count / (now - start)
    fpsImage = my_font.render(str(fps), True, WHITE)

    # Draw / render
    screen.fill(BLACK)
    screen.blit(fpsImage, (10, 100))
    # *after* drawing everything, flip the display
    pygame.display.flip()

    # *after* drawing everything, flip the display
    pygame.display.flip()  # 显示刚刚在内存中的所画的东西来展示到界面

pygame.quit()