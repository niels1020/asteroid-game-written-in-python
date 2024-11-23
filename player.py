from typing import List, Tuple
import pygame
import graphics
import settings
import main
import utils

player_model: List[Tuple[int, int]] = [(0, 20), (10, 10), (10, -10), (-10, -10), (-10, 10)]
angle: float = 0.0
position = pygame.Vector2(0,0)
rotation_weight = 0.1
speed = 1

def draw():
    screen_mid = utils.get_screen_midle()
    
    processed_model = [pygame.Vector2(point).rotate(angle-90) + screen_mid for point in player_model]
    
    graphics.outline_polygon(settings.primary_color, processed_model)
