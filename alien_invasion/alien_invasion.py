import sys
import pygame
from alien_invasion import *
from settings import Settings
from ship import Ship
from game_functions import *


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 设置背景颜色，免得单调和视疲劳
    # bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        check_events(ship)
        # 根据移动标志调整飞船的位置
        ship.update()
        # 更新屏幕
        update_screen(ai_settings, screen, ship)


run_game()
