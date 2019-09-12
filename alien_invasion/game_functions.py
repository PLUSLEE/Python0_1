import sys
import pygame


def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # ship.rect.centerx += 1
                ship.move_right = True
            elif event.key == pygame.K_LEFT:
                ship.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(ai_settings, screen, ship):
    # 每次循环重新绘制屏幕底色
    # screen.fill(bg_color)
    screen.fill(ai_settings.bg_color)

    # 指定位置绘制飞船
    ship.blitme()

    # 绘制屏幕
    pygame.display.flip()
