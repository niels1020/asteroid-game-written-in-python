import pygame
import graphics
import main
import settings
import math

def mouse_in_rect(rect: pygame.Rect):
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    if rect.topleft[0] < x and x < rect.topright[0]:
        if rect.topleft[1] < y and y < rect.bottomleft[1]:
            return True

    return False

def debug_draw():
    graphics.draw_text("fps: "+str(main.fps)+"  delta: "+str(main.delta), settings.debug_color, settings.debug_text_pos, settings.debug_text_size)

def get_screen_midle() -> pygame.Vector2:
    return pygame.Vector2(graphics.get_width()/2,graphics.get_height()/2)

def get_angle_between(a: pygame.Vector2,b: pygame.Vector2) -> float:
    dir: pygame.Vector2 = b - a
    angle_radians = math.atan2(dir.y, dir.x)
    angle_degrees = angle_radians * 180.0 / math.pi

    if (angle_degrees < 0): angle_degrees += 360.0
    return angle_degrees