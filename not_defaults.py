import pygame, os
from math import pi as PI

NOT_SCREEN_WIDTH, NOT_SCREEN_HEIGHT = (640, 480)
NOT_MENU_WIDTH, NOT_MENU_HEIGHT = (200, 480)

NOT_FRAME_RATE = 1000

NOT_TIME_UNIT = 0.05
NOT_SHOOTING_POWER_UNIT = 0.05
NOT_SHOOTING_ANGLE_CHANGE = PI / 500
NOT_GRAV = 3
NOT_GRAV_WORM = 3
NOT_JUMP_POWER = 15
NOT_WORM_SPEED = 1

NOT_PL, NOT_EN = "PL", "ENG"
NOT_ON, NOT_OFF = "ON", "OFF"

NOT_GUNPOINT_RADIUS = 10
NOT_GUNPOINT_CIRCLE_RADIUS = 2

NOT_BULLET_PATH = os.path.join("graphics", "RainbowBall.png")
NOT_player1_image_paths = os.listdir("graphics/Males")
NOT_player2_image_paths = os.listdir("graphics/Females")

NOT_PLAYER_1, NOT_PLAYER_2 = 1, 2

NOT_WHITE = (255, 255, 255)
NOT_BLACK = (0, 0, 0)
NOT_BLUE = (0, 0, 255)
NOT_RED = (255, 0, 0)
NOT_GREEN = (0, 255, 0)

NOT_hit_sound_paths = os.listdir("sounds/hits")

